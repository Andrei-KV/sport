from django.db import models
from django.urls import reverse

class SportCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name='Category title')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Category')
    def __str__(self):
        return self.title    
    
    def get_absolute_url(self):
        return reverse('sportcategory', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Sport category'
        verbose_name_plural = 'Sport categories'
        ordering = ['title', 'id'] 

class PlaceTitle(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    address = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    sport_category = models.ForeignKey(SportCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title  
    
    def get_absolute_url(self):
        return reverse('place', kwargs={'place_slug': self.slug})

    class Meta:
        verbose_name = 'place title'
        verbose_name_plural = 'place titles'
        ordering = ['time_create', 'title']

class Description(models.Model):
    description = models.TextField(blank=True, verbose_name='place description')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    placetitle = models.OneToOneField(PlaceTitle, on_delete=models.CASCADE, primary_key=True, verbose_name='Place title')

    def __str__(self):
        return self.description 

    class Meta:
        verbose_name = 'place description'
        verbose_name_plural = 'places descriptions'
        ordering = ['description', 'placetitle_id'] 
    
class Image(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='image title')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    place_title = models.ForeignKey(PlaceTitle, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'place image'
        verbose_name_plural = 'places images'
        ordering = ['title', 'id'] 