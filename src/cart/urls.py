from django.urls import path
from .views import AddProductToCart

app_name = 'cart'

urlpatterns = [
    path('add/', AddProductToCart.as_view(), name='add'),

]