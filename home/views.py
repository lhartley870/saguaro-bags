from django.shortcuts import render
from django.views.decorators.cache import cache_control


# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    """ View to render the index page """
    return render(request, 'home/index.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def privacy_policy(request):
    """ View to render the privacy policy page """
    return render(request, 'home/privacy_policy.html')
