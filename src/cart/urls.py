from django.urls import path
from .views import AddProductToCart, CartDetail, ProductInCartDelete

app_name = 'cart'

urlpatterns = [
    path('add/', AddProductToCart.as_view(), name='add'),
    path('cart/', CartDetail.as_view(), name='cart'),
    path('delete/<int:pk>', ProductInCartDelete.as_view(), name='delete'),
]