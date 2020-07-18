from django.urls import path
from .views import AddProductToCart, CartDetail

app_name = 'cart'

urlpatterns = [
    path('add/', AddProductToCart.as_view(), name='add'),
    path('cart/', CartDetail.as_view(), name='cart'),

]