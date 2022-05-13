from django.contrib import admin
from .models import Category, Size, Colour, Discount, Bag


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
    search_fields = ['name']

    ordering = ('friendly_name',)


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'order_smallest_to_largest',
    )

    ordering = ('order_smallest_to_largest',)


@admin.register(Colour)
class ColourAdmin(admin.ModelAdmin):

    ordering = ('name',)
    search_fields = ['name']


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'discount_amount_as_percentage',
    )
    list_filter = ('amount',)

    ordering = ('amount',)


@admin.register(Bag)
class BagAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sku',
        'category',
        'size',
        'colour',
        'original_price',
        'has_charm_option',
        'overall_rating',
        'on_sale',
        'discount_amount',
    )
    list_filter = ('category', 'size', 'colour', 'has_charm_option', 'on_sale')
    search_fields = ['name']

    ordering = ('name',)

    def discount_amount(self, obj):
        """
        Method to return the bag's discount amount if the bag
        has a discount.
        """
        if obj.discount is not None:
            discount_amount = obj.discount.amount
            return f'{discount_amount} %'
