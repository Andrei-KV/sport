from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('addplace/', add_place, name='add_place'),
    path('login/', login, name='login'),
    path('place/<int:place_id>/', show_place, name='place'),
    path('sportcategory/<int:cat_id>/', show_category, name='sportcategory'),
]