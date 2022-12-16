from django import template
from place.models import *

register = template.Library()

@register.simple_tag()
def get_categories(filter=None):
    if not filter:
        return SportCategory.objects.all()
    else:
        return SportCategory.objects.get(slug=filter)

@register.inclusion_tag('place/list_categories.html')
def show_category(sort=None, cat_selected=0):
    if not sort:
        cats =  SportCategory.objects.all()
    else:
        cats =  SportCategory.objects.order_by(sort)
    return {"cats": cats, "cat_selected": cat_selected}

@register.simple_tag()
def get_addresses_by_cat(cat_selected=0):
    if cat_selected == 0:
        return PlaceTitle.objects.all()
    else:
        sport_category_id = SportCategory.objects.get(slug=cat_selected).pk
        return PlaceTitle.objects.filter(sport_category_id=sport_category_id)