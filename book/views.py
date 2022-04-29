from urllib import response
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import typ_dania, danie, skladniki

# Create your views here.

def lista(request):
    lista_dan = danie.objects.order_by('nazwa_dania')[:5]
    context = {'lista_dan': lista_dan}
    return render(request, 'book/lista.html', context)

def przepis(request, danie_id):
    Danie = danie.objects.get(pk=danie_id)
    Przepis = skladniki.objects.filter(danie__przepis=True)
    return render(request, 'book/przepis.html', {'Danie': Danie, 'Przepis': Przepis})

