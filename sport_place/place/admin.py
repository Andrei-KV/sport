from django.contrib import admin
from .models import *

class SportCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class PlaceTitleAdmin(admin.ModelAdmin):
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
    prepopulated_fields = {'slug': ('title',)}

class DescriptionAdmin(admin.ModelAdmin):
    list_display = ( 'placetitle', 'photo', 'description',)
    list_display_links = ('placetitle',)
    search_fields = ('placetitle',)

class ImageAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'photo', 'place_title',)
    list_display_links = ('title',)
    search_fields = ('title', 'place_title',)    

admin.site.register(SportCategory, SportCategoryAdmin)
admin.site.register(PlaceTitle, PlaceTitleAdmin)
admin.site.register(Description, DescriptionAdmin)  
admin.site.register(Image, ImageAdmin)
