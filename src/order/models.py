from django.db import models

from cart.models import Cart
# Create your models here.
class Order(models.Model):
    cart = models.OneToOneField(
        Cart,
        on_delete=models.PROTECT,
        related_name = 'order'
    )
    status = models.BooleanField(
        "Is complete",
        default=False
    )
    delivery_address = models.TextField('Delivery Address')
    contact_phone = models.CharField("Contact Phone", max_length=50)
    created = models.DateTimeField(
        "Created",
        auto_now=False,
        auto_now_add=True
    )
    updated = models.DateTimeField(
        "Updated",
        auto_now=True,
        auto_now_add=False)