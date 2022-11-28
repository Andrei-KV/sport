from django.shortcuts import render
from django.http import HttpResponse

def index(request, place):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'Test page {place}')
