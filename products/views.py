from django.shortcuts import render
from .models import Bag


# Create your views here.
def all_bags(request):
    """ A view to show all bags, including sorting and search queries """
    bags = Bag.objects.all()
    context = {
        'bags': bags,
    }

    return render(request, 'products/bags.html', context)
