from django import template
from place.models import *

register = template.Library()

@register.simple_tag()
def get_categories(filter=None):
    if not filter:
        return SportCategory.objects.all()
    else:
        return SportCategory.objects.filter(pk=filter)

@register.inclusion_tag('place/list_categories.html')
def show_category(sort=None, cat_selected=0):
    if not sort:
        cats =  SportCategory.objects.all()
    else:
        cats =  SportCategory.objects.order_by(sort)
    return {"cats": cats, "cat_selected": cat_selected}

@register.simple_tag()
def get_addresses(cat_selected=0):
    if cat_selected == 0:
        return Address.objects.all()
    else:
        return Address.objects.filter(sport_category_id=cat_selected)