from django.shortcuts import render
from .forms import SubscriberForm
from products.models import Product, ProductImage

# Create your views here.
def landing(request):
  
    form = SubscriberForm(request.POST or None)
    if request.POST and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data['name'])

        form_new = form.save()

    return render(request, 'landing.html', locals())



def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True)
    return render(request, 'home.html', locals())