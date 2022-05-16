from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Bag, Charm


def basket_contents(request):

    basket_items = []
    total = 0
    bag_count = 0
    basket = request.session.get('basket', {})

    for item_id, item_data in basket.items():
        # If the item_data is an integer, the bag has no charm option
        if isinstance(item_data, int):
            bag = get_object_or_404(Bag, pk=item_id)
            # If the bag is on sale, use the discounted price.
            if bag.on_sale and bag.discount is not None:
                total += item_data * bag.get_discounted_price()
            # If the bag is not on sale use the original price.
            else:
                total += item_data * bag.original_price
            bag_count += item_data
            basket_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'bag': bag,
            })
        # If the item_data is not an integer, so the bag has a charm option
        else:
            bag = get_object_or_404(Bag, pk=item_id)
            for charm, quantity in item_data['items_by_charm_option'].items():        
                # If the bag is on sale, use the discounted price.
                if bag.on_sale and bag.discount is not None:
                    total += quantity * bag.get_discounted_price()
                # If the bag is not on sale use the original price.
                else:
                    total += quantity * bag.original_price
                bag_count += quantity
                if charm != 'No charm selected':
                    charm_id = int(charm)
                    charm_object = get_object_or_404(Charm, id=charm_id)
                else:
                    charm_object = None
                    charm = 'none'
                basket_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'bag': bag,
                    'charm_object': charm_object,
                    'charm': charm,
                })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE/100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'bag_count': bag_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
