from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_bags, name='bags'),
    path('<int:bag_id>', views.bag_detail, name='bag_detail'),
    path('add/', views.add_bag, name='add_bag'),
    path('edit/<int:bag_id>/', views.edit_bag, name='edit_bag'),
    path('delete/<int:bag_id>/',
         views.delete_bag,
         name='delete_bag'),
]
