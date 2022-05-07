from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)
    friendly_name = models.CharField(max_length=25, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Size(models.Model):
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.name


class Colour(models.Model):
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.name


class Discount(models.Model):
    name = models.CharField(max_length=25, unique=True)
    amount = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(99)
        ]
    )

    def __str__(self):
        return f'{self.amount} %'


class Bag(models.Model):
    name = models.CharField(max_length=25)
    sku = models.CharField(max_length=15, null=True, blank=True)
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    size = models.ForeignKey('Size', null=True, blank=True,
                             on_delete=models.SET_NULL)
    colour = models.ForeignKey('Colour', null=True, blank=True,
                               on_delete=models.SET_NULL)
    original_price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    image_description = models.TextField(null=True, blank=True)
    has_charm_option = models.BooleanField(default=False)
    overall_rating = models.DecimalField(max_digits=2, decimal_places=1,
                                         default=0.0)
    on_sale = models.BooleanField(default=False)
    discount = models.ForeignKey('Discount', null=True, blank=True,
                                 on_delete=models.SET_NULL)

    def __str__(self):
        return self.name