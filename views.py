from django.shortcuts import render
from .models import *

def livre(request):
    return render(request, 'livre/listeDeslivre.html')

def newLesen(request):
    new= newLesen.objects.all()

    return render(request, 'modeltest.html', {'new':new} )