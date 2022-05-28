from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

from checkout.models import Order
from .models import UserProfile
from .forms import UserProfileForm


# The solution of using the @cache_control and @login_required decorators
# to control what happens if a user logs out of their account and then
# presses the back button was taken from an answer given by Mahmood on
# this Stack Overflow post -
# https://stackoverflow.com/questions/28000981/django-user-re-entering
# -session-by-clicking-browser-back-button-after-logging?noredirect=1&lq=1
@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def profile(request):
    """ Display the user's profile. """

    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        form = UserProfileForm(instance=user_profile)

    orders = user_profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)


@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def order_history(request, order_number):
    """ Display the order details for a user's past order """

    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
