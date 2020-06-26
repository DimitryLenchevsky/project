from django.shortcuts import render
from .forms import SubscriberForm

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