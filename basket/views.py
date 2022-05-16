from django.shortcuts import render, redirect, get_object_or_404
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

    if 'charm_option' in request.POST:
        charm = request.POST['charm_option']

    bag = get_object_or_404(Bag, pk=item_id)
    if not charm and bag.has_charm_option:
        charm = 'No charm selected'

    if charm:
        if item_id in list(basket.keys()):
            if charm in basket[item_id]['items_by_charm_option'].keys():
                basket[item_id]['items_by_charm_option'][charm] += quantity
            else:
                basket[item_id]['items_by_charm_option'][charm] = quantity
        else:
            basket[item_id] = {'items_by_charm_option': {charm: quantity}}
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
        else:
            basket[item_id] = quantity

    request.session['basket'] = basket

    return redirect(redirect_url)
