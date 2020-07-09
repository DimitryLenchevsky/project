from django.shortcuts import render
from django.views.generic import DetailView
from . import models

# Create your views here.
class ProductView(DetailView):
    model = models.Product
    template_name = 'products/templates/detail.html'