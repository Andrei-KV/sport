from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import *

menu = [
    {'title': 'About', 'url_name': 'about',},
    {'title': 'Add place', 'url_name': 'add_place',},
    {'title': 'Log In', 'url_name': 'login'},
    ]

# def get_obj_or_404(cl, id):
#     try:
#         title = cl.objects.get(pk=id).title
#     except Exception:
#         raise Http404
#     return title

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
  
def show_place(request, place_slug):
    title = get_object_or_404(PlaceTitle, slug=place_slug)
    context = {
        'menu': menu, 
        'title': title.title,
        'cat_selected': title.sport_category_id,
        'place_slug': place_slug,
        'title': title,
    }
    return render(request, 'place/place.html', context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def show_category(request, cat_slug):
    category = get_object_or_404(SportCategory, slug=cat_slug)
    # try:
    #     title = SportCategory.objects.get(pk=cat_id).title
    # except Exception:
    #     raise Http404
    # addresses = Address.objects.filter(sport_category_id=cat_id)
    context = {
        # 'addresses': addresses,
        'menu': menu, 
        'title': category.title,
        'cat_selected': cat_slug,
        }
    return render(request, 'place/index.html', context)

