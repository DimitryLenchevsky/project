from django.shortcuts import render
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .models import Order
from cart.models import Cart
# Create your views here.
class CreateOrder(UpdateView):
    model = Order
    template_name = 'order/create.html'
    fields = (
        'delivery_address',
        'contact_phone'
    )
    success_url = reverse_lazy('products:list')
    def get_object(self):
        cart_id = self.request.session.get('cart_pk')
        if cart_id:
            cart = Cart.objects.get(pk=cart_id)
            try:
                order_pk = cart.order.pk
            except:
                order_pk = None

        obj, created = self.model.objects.get_or_create(
            pk=order_pk,
            defaults = {
                'cart' : cart,
                'status' : False,
                'delivery_address' : 'Type the address',
                'contact_phone' : 'Type the phone number',
            }
        )

        return obj


    def get_success_url(self):
        url = super().get_success_url()
        self.object.status = True
        self.object.save()
        del(self.request.session['cart_pk'])
        return url
