from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def test(request):

    # got data from DB
    data = [2, 4, 5, 6, 0, 34, 67, 23, 8, 3, 876, 32]
    r = random.randint(0, 100)
    context = {'some_value' : r, 'my_data' : data}
    return render(request, template_name="testapp/test.html", context=context)