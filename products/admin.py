from django.contrib import admin
from .models import Category, Size, Colour, Discount, Bag


# Register your models here.
admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Colour)
admin.site.register(Discount)
admin.site.register(Bag)
