import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Bag, Charm


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
    original_basket = models.TextField(default='')
    stripe_pid = models.CharField(max_length=254, default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            sdp = settings.STANDARD_DELIVERY_PERCENTAGE
            self.delivery_cost = self.order_total * sdp / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              related_name='lineitems')
    bag = models.ForeignKey(Bag, on_delete=models.CASCADE)
    bag_charm = models.ForeignKey(Charm, null=True, blank=True,
                                  on_delete=models.CASCADE)   
    quantity = models.IntegerField(default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        if self.bag.on_sale and self.bag.discount is not None:
            self.lineitem_total = (self.bag.get_discounted_price()
                                   * self.quantity)
        else:
            self.lineitem_total = self.bag.original_price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.bag.sku} on order {self.order.order_number}'
