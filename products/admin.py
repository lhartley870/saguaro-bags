from django.contrib import admin
from .models import Category, Size, Colour, Discount, Bag


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('friendly_name',)


@admin.register(Colour)
class ColourAdmin(admin.ModelAdmin):

    ordering = ('name',)


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        '__str__',
    )

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

    ordering = ('name',)


admin.site.register(Size)
