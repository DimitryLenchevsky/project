from django.urls import path
from .views import ProductView, ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = 'products'

urlpatterns = [
    path('product/<int:pk>', ProductView.as_view(), name='detail'),
    path('product-list/', ProductListView.as_view(), name='list'),
    path('product-create/', ProductCreateView.as_view(), name='create'),
    path('product-update/<int:pk>', ProductUpdateView.as_view(), name='update'),
    path('product-delete/<int:pk>', ProductDeleteView.as_view(), name='delete'),
]