from django.shortcuts import render
from django.http import HttpResponse

from . models import Genre
# Create your views here.


def test(request):

    # get one obj from Genre
    genres = Genre.objects.all()
    context = {'genres' : genres}
    return render(request, template_name="testapp/test.html", context=context)