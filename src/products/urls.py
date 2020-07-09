from django.urls import path
from .views import ProductView

app_name = 'products'

urlpatterns = [
    path('product/<int:pk>', ProductView.as_view(), name='detail'),
]