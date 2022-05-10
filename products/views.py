from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import Bag, Category


# Create your views here.
def all_bags(request):
    """ A view to show all bags, including sorting and search queries """
    bags = Bag.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            bags = bags.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter some search criteria")
                return redirect(reverse('bags'))

            bags = bags.filter(name__icontains=query)

    context = {
        'bags': bags,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products/bags.html', context)


def bag_detail(request, bag_id):
    """ A view to show individual bag details """
    bag = get_object_or_404(Bag, pk=bag_id)
    rating_stars = bag.get_number_rating_stars()
    if isinstance(rating_stars, list):
        whole_stars = rating_stars[0]
        whole_stars_list = list(range(1, rating_stars[0] + 1))
        half_stars_list = [1]
        empty_stars = 4 - whole_stars
        empty_stars_list = list(range(1, empty_stars + 1))
    else:
        whole_stars = rating_stars
        whole_stars_list = list(range(1, rating_stars + 1))
        half_stars_list = []
        empty_stars = 5 - whole_stars
        empty_stars_list = list(range(1, empty_stars + 1))

    context = {
        'bag': bag,
        'whole_stars': whole_stars_list,
        'half_stars': half_stars_list,
        'empty_stars': empty_stars_list,
    }

    return render(request, 'products/bag_detail.html', context)
