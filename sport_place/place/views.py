from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [
    {'title': 'About', 'url_name': 'about',},
    {'title': 'Add place', 'url_name': 'add_place',},
    {'title': 'Log In', 'url_name': 'login'},
    ]

def index(request):
    addresses = Address.objects.all()
    for i in addresses:
        print(i.pk, type(i.pk))
    context = {
        'addresses': addresses, 
        'menu': menu, 
        'title': 'Head page',
        }
    return render(request, 'place/index.html', context)

def about(request):
    return HttpResponse('About site')

def add_place(request):
    return HttpResponse('Add place')

def login(request):
    return HttpResponse('Log In')
  
def show_place(request, place_id):
    print(place_id)
    return HttpResponse(f'PLACE {place_id}')
   
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')