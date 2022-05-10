from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Bag, Category


# Create your views here.
def all_bags(request):
    """ A view to show all bags, including sorting and search queries """
    bags = Bag.objects.all()
    query = None
    categories = None
    sale = False
    free_charm = True
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'category':
                sortkey = 'category__name'
            if sortkey == 'colour':
                sortkey = 'colour__name'      
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
                    
            bags = bags.order_by(sortkey)

        # Filters the bags by category/style.
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            bags = bags.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # If only the 'Special Offers' dropdown of 'Sale Items' has been
        # selected
        if 'sale' in request.GET:
            # This ensures that if any store admin has accidentally
            # marked a bag as on sale but has failed to fill in the discount,
            # that bag will not show up as being on sale.
            bags = bags.filter(on_sale=True).exclude(discount=None)
            sale = True

        # If only the 'Special Offers' dropdown of 'Free Charm' has been
        # selected
        if 'free_charm' in request.GET:
            bags = bags.filter(has_charm_option=True)
            free_charm = True

        # If the 'All Special Offers' dropdown has been selected
        if 'all_special_offers' in request.GET:
            filters = Q(has_charm_option=True) | (Q(on_sale=True) & ~Q(discount=None))
            bags = bags.filter(filters)
            sale = True
            free_charm = True

        # Deals with search bar queries.
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter some search criteria")
                return redirect(reverse('bags'))

            bags = bags.filter(name__icontains=query)

    current_sorting = f'{sort}_{direction}'

    context = {
        'bags': bags,
        'search_term': query,
        'current_categories': categories,
        'sale': sale,
        'free_charm': free_charm,
        'current_sorting': current_sorting,
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
