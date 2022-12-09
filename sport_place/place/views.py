from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [
    {'title': 'About', 'url_name': 'about',},
    {'title': 'Add place', 'url_name': 'add_place',},
    {'title': 'Log In', 'url_name': 'login'},
    ]

def index(request):
    # addresses = Address.objects.all()
    context = {
        # 'addresses': addresses,
        'menu': menu, 
        'title': 'Head page',
        'cat_selected': 0,
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

def show_category(request, cat_id):
    try:
        title = SportCategory.objects.get(pk=cat_id).title
    except Exception:
        raise Http404
    # addresses = Address.objects.filter(sport_category_id=cat_id)
    context = {
        # 'addresses': addresses,
        'menu': menu, 
        'title': title,
        'cat_selected': cat_id,
        }
    return render(request, 'place/index.html', context)
