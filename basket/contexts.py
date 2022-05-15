from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Bag


def basket_contents(request):

    basket_items = []
    total = 0
    bag_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        bag = get_object_or_404(Bag, pk=item_id)
        # If the bag is on sale, use the discounted price.
        if bag.on_sale and bag.discount is not None:
            total += quantity * bag.get_discounted_price()
        # If the bag is not on sale use the original price.
        else:
            total += quantity * bag.original_price
        bag_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'bag': bag,
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
