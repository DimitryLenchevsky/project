from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from . import models
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.
class ProductView(DetailView):
    model = models.Product
    template_name = 'products/templates/detail.html'


class ProductListView(LoginRequiredMixin, ListView):
    model = models.Product
    template_name = 'products/templates/list.html'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        key1 = self.request.GET.get('key1')
        print(key1)
        context = super().get_context_data(**kwargs)
        context['key1'] = key1
        return context



class ProductCreateView(LoginRequiredMixin, CreateView):
    model = models.Product
    template_name = 'products/templates/create.html'
    fields = ('name', 'author', 'price', 'genre', 'description',)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Product
    template_name = 'products/templates/update.html'
    fields = ('name', 'author', 'price', 'genre', 'description',)
    def get_success_url(self):
        return reverse_lazy('products:detail', kwargs={'pk': self.object.pk})
    

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Product
    template_name = 'products/templates/delete.html'
    success_url = '/products/templates/list.html/'