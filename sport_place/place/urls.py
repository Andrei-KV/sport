from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('addplace/', add_place, name='add_place'),
    path('login/', login, name='login'),
    path('place/<slug:place_slug>/', show_place, name='place'),
    path('sportcategory/<slug:cat_slug>/', show_category, name='sportcategory'),
]
