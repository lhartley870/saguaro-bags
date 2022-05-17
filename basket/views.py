from django.shortcuts import render, redirect, get_object_or_404, reverse
from products.models import Bag


# Create your views here.
def view_basket(request):
    """ View to render the basket contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the chosen bag to the shopping basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    charm = None
    basket = request.session.get('basket', {})

    # If a charm option has been selected, charm
    # is set to that charm's id.
    if 'charm_option' in request.POST:
        charm = request.POST['charm_option']

    # If the bag has a charm option but no charm has
    # been selected, charm is set to 'No charm selected'.
    bag = get_object_or_404(Bag, pk=item_id)
    if not charm and bag.has_charm_option:
        charm = 'No charm selected'

    # If the submitted bag has a charm option.
    if charm:
        if item_id in list(basket.keys()):
            # If the submitted bag and charm combination is already in
            # the basket, increase the quantity.
            if charm in basket[item_id]['items_by_charm_option'].keys():
                basket[item_id]['items_by_charm_option'][charm] += quantity
            # If the submitted bag is already in the basket, but not with this
            # charm combination, add the charm key and the quantity.
            else:
                basket[item_id]['items_by_charm_option'][charm] = quantity
        # If the submitted bag is not already in the basket, add the new bag,
        # charm key and quantity.
        else:
            basket[item_id] = {'items_by_charm_option': {charm: quantity}}
    # If the submitted bag does not have a charm option.
    else:
        # If the submitted bag is already in the basket, increase the quantity.
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
        # If the submitted bag is not already in the basket, add the new bag
        # and quantity.
        else:
            basket[item_id] = quantity

    request.session['basket'] = basket

    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """
    Adjust the quantity of the specified bag (and charm combination if
    applicable) to the specified amount.
    """

    quantity = int(request.POST.get('quantity'))
    charm = None
    basket = request.session.get('basket', {})

    if 'charm_option' in request.POST:
        # If the 'charm_option' value is not 'none'
        # then the user has selected a charm.
        if request.POST['charm_option'] != 'none':
            charm = request.POST['charm_option']
        # If the 'charm_option' value is 'none', the
        # user had the option to choose a charm but
        # didn't.
        else:
            charm = 'No charm selected'

    if charm:
        if quantity > 0:
            basket[item_id]['items_by_charm_option'][charm] = quantity
        else:
            del basket[item_id]['items_by_charm_option'][charm]
    else:
        if quantity > 0:
            basket[item_id] = quantity
        else:
            basket.pop(item_id)

    request.session['basket'] = basket

    return redirect(reverse('view_basket'))
