from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


# Create your views here.
def checkout(request):
    """ View to render the checkout page """

    basket = request.session.get('basket', {})
    # If there is nothing in the basket, render error message
    # and redirect back to the all bags page.
    if not basket:
        messages.error(request,
                       'There is nothing in your basket at the moment')
        return redirect(reverse('bags'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
