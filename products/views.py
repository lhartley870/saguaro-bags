from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import When, Case, F, Q
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
        # Deals with the 'All Bags' main navbar options to sort
        # the bags by price, rating, style, size and colour.
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            # Sorting by style sorts by the style/category name.
            if sortkey == 'category':
                sortkey = 'category__name'
            # Sorting by colour, sorts by the colour name.
            if sortkey == 'colour':
                sortkey = 'colour__name'
            # Sorting by size, sorts by the 'order_smallest_to_largest'
            # integer number given to the size by the site admin.
            if sortkey == 'size':
                sortkey = 'size__order_smallest_to_largest'
            # Sorting by price annotates each bag object with a final_price.
            # The final_price is the bag's original price if on_sale is False.
            # The final_price is the bag's discounted price if on_sale is True
            # AND the discount is not None (to filter out cases where the admin
            # may have marked the bag as on sale but failed to fill in the
            # discount). The default value is the bag's original price, which
            # will catch any bags marked as on_sale where the admin has failed
            # to fill in the discount.
            if sortkey == 'price':
                sortkey = 'final_price'
                bags = bags.annotate(
                    final_price=Case(
                        When(
                            on_sale=False,
                            then=(F('original_price')),
                        ),
                        When(
                            Q(on_sale=True) & ~Q(discount=None),
                            then=F('original_price') -
                            (
                                F('original_price') *
                                F('discount__amount') /
                                100
                            ),
                        ),
                        default=F('original_price')
                    )
                )
            # Sorting by bag name sorts by the lowercase names.
            if sortkey == 'name':
                sortkey = 'lower_name'
                bags = bags.annotate(lower_name=Lower('name'))

            # Deals with any sorting of the bags being in descending order.
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            bags = bags.order_by(sortkey)

        # Filters the bags by category/style in the main navbar 'Styles'
        # dropdown.
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            bags = bags.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # Applies if the 'Special Offers' dropdown of 'Sale Items' in the main
        # navbar has been selected.
        if 'sale' in request.GET:
            # This ensures that if any store admin has accidentally
            # marked a bag as on sale but has failed to fill in the discount,
            # that bag will not show up as being on sale.
            bags = bags.filter(on_sale=True).exclude(discount=None)
            sale = True

        # Applies if the 'Special Offers' dropdown of 'Free Charm' in the main
        # navbar has been selected.
        if 'free_charm' in request.GET:
            bags = bags.filter(has_charm_option=True)
            free_charm = True

        # Applies if the 'Special Offers' dropdown of 'All Special Offers' in
        # the main navbar has been selected.
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
