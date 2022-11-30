from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = ["About", "Add place", "Log In"]

def index(request):
    addresses = Address.objects.all()
    adr_cat_dict = {}
    for i in addresses:
        adr_cat_dict[i.title] = [i.sport_category.title, i.description.description]
    return render(request, 'place/index.html', {'adr_cat_dict': adr_cat_dict, 'menu': menu, 'title': 'Head page'})

def about(request):
    return render(request, 'place/index.html', {'menu': menu, 'title': 'About site'})


def categories(request, catid):
    if request.POST:
        print(request.POST)

    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")

def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=False)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')