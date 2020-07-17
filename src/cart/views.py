from django.shortcuts import render
from django.views.generic import UpdateView
from products.models import Product, ProductGenre, ProductImage
from . import models

class AddProductToCart(UpdateView):
    models = models.ProductInCart
    template_name = 'cart/add.html'
    fields = ('quantity',)

    def get_object(self):
        cart_pk=self.request.session.get('cart_pk', None)
        product_pk=self.request.GET.get('product_pk')
        product = Product.objects.get(pk=int(product_pk))
        user = self.request.user
        cart, create = models.Cart.objects.get_or_create(
            pk=int(cart_pk),
            user=user,
            defaults={},
        )
        if create:
            self.request.session['cart_pk'] = cart.pk
        obj, create = self.models.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={},
        )
        return obj # Inst models.ProductInCart