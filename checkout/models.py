from django.db import models
from django_countries.fields import CountryField


class Order(models.Model):
    order_number = models.CharField(max_length=32, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=20)
    street_address1 = models.CharField(max_length=80)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='Country *')
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2,
                                        default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      default=0)
