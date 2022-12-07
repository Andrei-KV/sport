from django.contrib import admin
from .models import *

class SportCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 
        'address', 
        'time_create', 'time_update',
        'is_published',
        'sport_category'
        )
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    list_filter = ('is_published',  'time_create',)
    search_fields = ('title', 'address')

class DescriptionAdmin(admin.ModelAdmin):
    list_display = ('description', 'photo', 'address')
    list_display_links = ('address',)
    search_fields = ('address',)

admin.site.register(SportCategory, SportCategoryAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Description, DescriptionAdmin)  
