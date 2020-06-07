from django.shortcuts import render
from django.http import HttpResponse
from . models import Genre, Book
from . forms import CreateGenreForm
# Create your views here.


def test(request, pk):

    #obj.Genre(name=name, description=description)
    post_data = request.POST
    name = request.POST.get('name')
    description = request.POST.get('description')
    obj = Genre.objects.get(pk=pk)

    form = CreateGenreForm({'name': obj.name, 'description': obj.description})

    print(request.method)
    
    #obj.save()
    #books = Book.objects.all()
    context = {'form' : form}
    return render(request, template_name="testapp/test.html", context=context)