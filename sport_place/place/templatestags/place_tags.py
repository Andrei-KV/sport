from django import template
from place.models import *

register = template.Library()

@register.simple_tag()
def get_categories():
    return SportCategory.objects.all()