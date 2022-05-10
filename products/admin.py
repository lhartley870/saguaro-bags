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
        'discount',
    )
    list_filter = ('category', 'size', 'colour', 'has_charm_option', 'on_sale')
    search_fields = ['name']

    ordering = ('name',)


admin.site.register(Size)
