from django.shortcuts import render
from django.views.generic import UpdateView, DetailView, DeleteView
from products.models import Product, ProductGenre, ProductImage
from django.urls import reverse_lazy
from . import models


def get_cart(request):
    cart_pk=request.session.get('cart_pk')
    user = request.user
    if user.is_anonymous:
        user = None
    if cart_pk is not None:
        cart_pk = int(cart_pk)
    cart, create = models.Cart.objects.get_or_create(
        pk=cart_pk,
        defaults={
            'user': user,
        },
    )
    return cart, create

class AddProductToCart(UpdateView):
    models = models.ProductInCart
    template_name = 'cart/add.html'
    fields = ('quantity',)
    success_url = '/product-list/'

    def get_object(self):
        product_pk=self.request.GET.get('product_pk')
        product = Product.objects.get(pk=int(product_pk))
        cart, create = get_cart(self.request)
        if create:
            self.request.session['cart_pk'] = cart.pk
        obj, create = self.models.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={}
        )
        return obj # Inst models.ProductInCart



class CartDetail(DetailView):
    model = models.Cart
    template_name = 'cart/cart.html'
    def get_object(self):
        cart = get_cart(self.request)
        cart, create = get_cart(self.request)
        if create:
            self.request.session['cart_pk'] = cart.pk
        return cart


class ProductInCartDelete(DeleteView):
    model = models.ProductInCart
    template_name = 'cart/delete.html'
    success_url = reverse_lazy('cart:cart')