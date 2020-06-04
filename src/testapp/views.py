from django.shortcuts import render
from django.http import HttpResponse

from . models import Parsing
import dz17052020
# Create your views here.


def test(request):

    name_safari = dz17052020.saf
    name_firefox = dz17052020.ff

    safari17 = dz17052020.safari17
    sa17 = len(safari17)

    safari18 = dz17052020.safari18
    sa18 = len(safari18)

    safari19 = dz17052020.safari19
    sa19 = len(safari19)

    safari20 = dz17052020.safari20
    sa20 = len(safari20)

    firefox17 = dz17052020.firefox17
    ff17 = len(firefox17)

    firefox18 = dz17052020.firefox18
    ff18 = len(firefox18)

    firefox19 = dz17052020.firefox19
    ff19 = len(firefox19)

    firefox20 = dz17052020.firefox20
    ff20 = len(firefox20)
    
    
    parsing = Parsing.objects.all()
    context = {'parsing' : parsing, 
    'name_safari' : name_safari, 'name_firefox' : name_firefox, 
    'sa17' : sa17, 'sa18' : sa18, 'sa19' : sa19, 'sa20' : sa20,
    'ff17' : ff17, 'ff18' : ff18, 'ff19' : ff19, 'ff20' : ff20}
    return render(request, template_name="testapp/test.html", context=context)