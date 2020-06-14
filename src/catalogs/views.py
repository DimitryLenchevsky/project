from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from . import models
 
class PhoneTypeListView(ListView):
    model = models.PhoneType
    template_name = 'catalogs/list.html' 


class CreatePhoneTypeView(CreateView):
    model = models.PhoneType
    template_name = 'catalogs/create.html'
    fields = ('name',)


class UpdatePhoneTypeView(UpdateView):
    model = models.PhoneType
    template_name = 'catalogs/update.html'
    #success_url = '/catalogs/create-phone-type/'
    #success_url = '/catelogs/phone-type/{{ obj.pk }}'
    fields = ('name',)
    def get_success_url(self):
        return reverse_lazy('catalogs:detail', kwargs={'pk': self.object.pk})
        #return f'/catalogs/phone-type/{ self.object.pk }'


class DeletePhoneTypeView(DeleteView):
    model = models.PhoneType 
    template_name = 'catalogs/delete.html'
    success_url = '/catalogs/create-phone-type/'


class PhoneTypeView(DetailView):
    model = models.PhoneType
    template_name = 'catalogs/detail.html'
