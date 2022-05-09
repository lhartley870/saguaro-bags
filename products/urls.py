from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_bags, name='bags'),
    path('<int:bag_id>', views.bag_detail, name='bag_detail'),
]
