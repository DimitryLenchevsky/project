from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product, ProductGenre, ProductImage

# Create your models here.
User = get_user_model()
class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='carts',
        blank=True,
        null=True
    )

    def __str__(self):
        return f'Cart #{self.pk}'

    @property
    def total_price(self):
        total_price = 0
        for good in self.products.all():
            total_price += good.total_price
        return total_price


class ProductInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='products',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='products_in_cart',
    )
    quantity = models.IntegerField(
        verbose_name='Quantity',
        default=1,
    )

    def __str__(self):
        return f'Product #{self.product.name} in cart #{self.cart.pk}'
    
    @property
    def total_price(self):
        total_price = self.quantity * self.product.price
        return total_price

    class Meta:
        unique_together = (('cart', 'product'),)