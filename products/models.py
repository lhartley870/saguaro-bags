from decimal import Decimal
import math
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)
    friendly_name = models.CharField(max_length=25, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.friendly_name


class Size(models.Model):
    name = models.CharField(max_length=25, unique=True)
    order_smallest_to_largest = models.PositiveSmallIntegerField(
        unique=True,
        validators=[MinValueValidator(1)]
    )

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
        return self.name

    def discount_amount_as_percentage(self):
        """
        Shows the discount amount as a percentage.
        """
        return f'{self.amount} %'


class Bag(models.Model):
    name = models.CharField(max_length=25, unique=True)
    sku = models.CharField(max_length=15, unique=True)
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

    def get_discounted_price(self):
        """
        Method to calculate the discounted price of a bag if it is on sale.

        A check is performed in the bags.html template to check for bags where
        on_sale is True but the discount is None (to cover any human error
        where the admin may have marked the bag as on_sale but has failed to
        complete the discount field) to ensure such bags are not displayed as
        being on sale with the original_price being struck through. The if
        statement in this method is a back up to the template check. If the
        discount is not None, the new price is calculated to 2 decimal places,
        otherwise the original_price is returned.
        """
        if self.discount is not None:
            # Use of the Decimal module and the quantize method to calculate
            # the discounted price and return it to 2 decimal places taken from
            # the Python documentation -
            # https://docs.python.org/3/library/decimal.html#decimal-faq
            discount = (Decimal(self.discount.amount / 100)
                        * self.original_price)
            discounted_price = self.original_price - discount
            two_places = Decimal(10) ** -2

            return discounted_price.quantize(two_places)
        else:
            return self.original_price


    def get_number_rating_stars(self):
        """
        Method to work out the number of full stars, half stars
        and empty stars to be shown in the rating for each bag for sale.
        """
        rating = self.overall_rating
        # Use of divmod to find out the integer and decimal
        # parts of a float taken from an answer given by utdemir
        # on this Stack Overflow post -
        # https://stackoverflow.com/questions/6681743/splitting-a-
        # number-into-the-integer-and-decimal-parts
        i, d = divmod(rating, 1)
        # If the decimal is less than .5, round down to the nearest
        # whole number and return that.
        if d < 0.5:
            return math.floor(self.overall_rating)
        # If the decimal is .5, return the integer in a list.
        elif d == 0.5:
            return [int(i)]
        # If the decimal is more than .5, round up to the nearest
        # whole number and return that.
        elif d > 0.5:
            return math.ceil(self.overall_rating)


class Charm(models.Model):
    name = models.CharField(max_length=25, unique=True)
    image = models.ImageField()
    image_description = models.TextField()

    def __str__(self):
        return self.name
