from django.contrib import admin
from . models import Cart, ProductInCart

# Register your models here.
admin.site.register(Cart)
admin.site.register(ProductInCart)