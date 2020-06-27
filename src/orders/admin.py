from django.contrib import admin
from .models import Order, Status, ProductInOrder

# Register your models here.
class ProductInOrderInline(admin.TabularInline):
    
    model = ProductInOrder
    extra = 0


class OrderAdmin(admin.ModelAdmin):

    list_display = (
        'pk',
        'customer_name', 
        'customer_email', 
        'customer_phone', 
        'status', 
        'comments', 
        'created', 
        'updated',
        'total_price',
        )
    inlines = [ProductInOrderInline]

    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)

class StatusAdmin(admin.ModelAdmin):

    list_display = (
        'pk',
        'name', 
        'is_active', 
        'comments', 
        'created', 
        'updated',
        )
    

    class Meta:
        model = Status

admin.site.register(Status, StatusAdmin)


class ProductInOrderAdmin(admin.ModelAdmin):

    list_display = (
        'pk',
        'order', 
        'product', 
        'is_active', 
        'created', 
        'updated',
        'price_per_item',
        'total_price',
        )

    class Meta:
        model = ProductInOrder

admin.site.register(ProductInOrder, ProductInOrderAdmin)