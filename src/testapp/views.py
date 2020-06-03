from django.shortcuts import render
from django.http import HttpResponse

from . models import Genre, Book
# Create your views here.


def test(request):

    # get one obj from Genre
    genres = Genre.objects.all()
    books = Book.objects.all()
    context = {'genres' : genres, 'books' : books}
    return render(request, template_name="testapp/test.html", context=context)