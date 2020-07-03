from django.contrib import admin
from .models import Product, ProductImage, ProductGenre

# Register your models here.

class ProductImageInline(admin.TabularInline):
    
    model = ProductImage
    extra = 0


class ProductGenreAdmin(admin.ModelAdmin):

    list_display = (
        'pk',
        'name',
        'is_active',
    )
    class Meta:
        model = ProductGenre
admin.site.register(ProductGenre, ProductGenreAdmin)

class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'pk',
        'name',
        'author',
        'price',
        'genre',
        'description',
        'is_active',
        'created',
        'updated',
        )
    inlines = [ProductImageInline]

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)


class ProductImageAdmin(admin.ModelAdmin):

    list_display = (
        'product',
        'image',
        'is_active',
        'is_main',
        'created',
        'updated',
        )

    class Meta:
        model = ProductImage

admin.site.register(ProductImage, ProductImageAdmin)