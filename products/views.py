from django.shortcuts import render, get_object_or_404
from .models import Bag


# Create your views here.
def all_bags(request):
    """ A view to show all bags, including sorting and search queries """
    bags = Bag.objects.all()
    context = {
        'bags': bags,
    }

    return render(request, 'products/bags.html', context)


def bag_detail(request, bag_id):
    """ A view to show individual bag details """
    bag = get_object_or_404(Bag, pk=bag_id)
    context = {
        'bag': bag,
    }

    return render(request, 'products/bag_detail.html', context)
