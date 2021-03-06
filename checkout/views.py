import json

from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.views.decorators.cache import cache_control

import stripe

from basket.contexts import basket_contents

from products.models import Bag, Charm
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from .forms import OrderForm
from .models import Order, OrderLineItem


@require_POST
def cache_checkout_data(request):
    """ View to add additional metadata to payment intent object """

    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, ('Sorry, your payment cannot be '
                                 'processed right now. Please try '
                                 'again later.'))
        return HttpResponse(content=e, status=400)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def checkout(request):

    """ View to render the checkout page """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        basket = request.session.get('basket', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_basket = json.dumps(basket)
            order.save()
            for item_id, item_data in basket.items():
                try:
                    bag = Bag.objects.get(id=item_id)
                    # If the item_data is an integer, the bag has no charm
                    # option
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            bag=bag,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    # If the item_data is not an integer, the bag has a charm
                    # option
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
                # This should not happen, but in case a bag in the basket
                # does not exist, an error message is rendered, the order
                # is deleted and user is returned to the shopping basket page.
                except Bag.DoesNotExist:
                    messages.error(request, (
                        "One of the items in your basket wasn't "
                        "found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_basket'))

            # Save the info to the user's profile if all is well
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            messages.error(request, ('There was an error with your form. '
                                     'Please double check your information.'))
    else:
        basket = request.session.get('basket', {})
        # If there is nothing in the basket, render error message
        # and redirect back to the all bags page.
        if not basket:
            messages.error(request,
                           'There is nothing in your basket at the moment')
            return redirect(reverse('bags'))

        current_basket = basket_contents(request)
        total = current_basket['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Attempt to prefill the form with any info
        # the user maintains in their profile
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'town_or_city': profile.default_town_or_city,
                    'county': profile.default_county,
                    'postcode': profile.default_postcode,
                    'country': profile.default_country,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    # If stripe public key is missing render error message.
    if not stripe_public_key:
        messages.warning(request, ('Stripe public key is missing. '
                                   'Did you forget to set it in '
                                   'your environment?'))

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """

    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    # The if statement is triggered when a registered user logs out
    # and then uses the back button to try and navigate back to the checkout
    # success page. In this circumstance, the user will not be able to
    # see the checkout success page and will instead be redirected to the
    # login page. Used to protect the user's data visible on the checkout
    # success page.
    if order.user_profile is not None and request.user.is_anonymous:
        return redirect(reverse('account_login'))
    else:
        if request.user.is_authenticated:
            profile = UserProfile.objects.get(user=request.user)
            # Attach the user's profile to the order
            order.user_profile = profile
            order.save()

            # Save the user's info
            if save_info:
                profile_data = {
                    'default_phone_number': order.phone_number,
                    'default_street_address1': order.street_address1,
                    'default_street_address2': order.street_address2,
                    'default_town_or_city': order.town_or_city,
                    'default_county': order.county,
                    'default_postcode': order.postcode,
                    'default_country': order.country,
                }
                user_profile_form = UserProfileForm(
                                                    profile_data,
                                                    instance=profile)
                if user_profile_form.is_valid():
                    user_profile_form.save()

        messages.success(request, f'Order successfully processed! '
                         f'Your order number is {order_number}. '
                         f'A confirmation email will be sent to '
                         f'{order.email}.')

        # Clear the shopping basket in session storage.
        if 'basket' in request.session:
            del request.session['basket']

        template = 'checkout/checkout_success.html'
        context = {
            'order': order,
        }

        return render(request, template, context)
