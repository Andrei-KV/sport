from django.db import models
from django.urls import reverse

class SportCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name='Category title')
    
    def __str__(self):
        return self.title    
    
    def get_absolute_url(self):
        return reverse('sportcategory', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Sport category'
        verbose_name_plural = 'Sport categories'
        ordering = ['title', 'id'] 

class Address(models.Model):
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    sport_category = models.ForeignKey(SportCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title  
    
    def get_absolute_url(self):
        return reverse('place', kwargs={'place_id': self.pk})

    class Meta:
        verbose_name = 'place address'
        verbose_name_plural = 'place addresses'
        ordering = ['time_create', 'title']

class Description(models.Model):
    description = models.TextField(blank=True, verbose_name='place description')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, primary_key=True, verbose_name='Place title')
    

    def __str__(self):
        return self.description 

    class Meta:
        verbose_name = 'Place description'
        verbose_name_plural = 'Places descriptions'
        ordering = ['description', 'address_id'] 
    
