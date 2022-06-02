import json
import time

from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.shortcuts import get_object_or_404

from products.models import Bag, Charm
from profiles.models import UserProfile
from .models import Order, OrderLineItem


class StripeWH_Handler:
    """ Handle Stripe webhooks """

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """ Send the user a confirmation email """
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        # Extract data from the Stripe payment intent object.
        pid = intent.id
        basket = intent.metadata.basket
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details.
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information if save_info was checked.
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            address_line_1 = shipping_details.address.line1
            address_line_2 = shipping_details.address.line2
            if save_info:
                profile.default_phone_number = shipping_details.phone
                profile.default_street_address1 = address_line_1
                profile.default_street_address2 = address_line_2
                profile.default_town_or_city = shipping_details.address.city
                profile.default_county = shipping_details.address.state
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_country = shipping_details.address.country
                profile.save()

        order_exists = False
        attempt = 1
        # Check if the order has already been created by the checkout view.
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            # Try to find the order 5 times over 5 seconds, in case the
            # checkout view is slow creating it.
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        # If the order already exists, return 200 HTTP response to Stripe.
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=(f'Webhook received: {event["type"]} | SUCCESS: '
                         'Verified order already in database'),
                status=200)
        # If the order does not already exist e.g. because of a user error
        # during the checkout process, try to create the order.
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(basket).items():
                    bag = Bag.objects.get(id=item_id)
                    # If the item_data is an integer, the bag has no charm
                    # option.
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            bag=bag,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    # If the item_data is not an integer, the bag has a charm
                    # option.
                    else:
                        for charm, quantity in item_data[
                                                        'items_by_charm_option'
                                                        ].items():
                            # If a charm has been selected
                            if charm != 'No charm selected':
                                charm_id = int(charm)
                                bag_charm = get_object_or_404(Charm,
                                                              id=charm_id)
                                order_line_item = OrderLineItem(
                                    order=order,
                                    bag=bag,
                                    quantity=quantity,
                                    bag_charm=bag_charm,
                                )
                            # If a charm has not been selected
                            else:
                                order_line_item = OrderLineItem(
                                    order=order,
                                    bag=bag,
                                    quantity=quantity,
                                )
                            order_line_item.save()

            # If something goes wrong with trying to create the order,
            # delete any order created and return a 500 server error
            # response to Stripe.
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order)
        # If the order has been created by the webhook handler, return 200
        # HTTP response to Stripe.
        return HttpResponse(
            content=(f'Webhook received: {event["type"]} | SUCCESS: '
                     'Created order in webhook'),
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe.
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
