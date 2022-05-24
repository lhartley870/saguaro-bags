from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

import stripe

from basket.contexts import basket_contents

from .forms import OrderForm


# Create your views here.
def checkout(request):
    """ View to render the checkout page """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

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

    if not stripe_public_key:
        messages.warning(request, ('Stripe public key is missing. '
                                   'Did you forget to set it in '
                                   'your environment?'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
