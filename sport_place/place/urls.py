from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('place/<slug:place>/', index, name='home')
]