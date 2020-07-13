from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from . import models
from django.urls import reverse_lazy

# Create your views here.
class ProductView(DetailView):
    model = models.Product
    template_name = 'products/templates/detail.html'


class ProductListView(ListView):
    model = models.Product
    template_name = 'products/templates/list.html'


class ProductCreateView(CreateView):
    model = models.Product
    template_name = 'products/templates/create.html'
    fields = ('name', 'author', 'price', 'genre', 'description',)


class ProductUpdateView(UpdateView):
    model = models.Product
    template_name = 'products/templates/update.html'
    fields = ('name', 'author', 'price', 'genre', 'description',)
    def get_success_url(self):
        return reverse_lazy('products:detail', kwargs={'pk': self.object.pk})
    

class ProductDeleteView(DeleteView):
    model = models.Product
    template_name = 'products/templates/delete.html'
    success_url = '/products/templates/list.html/'