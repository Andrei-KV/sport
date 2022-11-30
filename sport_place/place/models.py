from django.db import models

class SportCategory(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title    

class Address(models.Model):
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateField(auto_now=True)
    is_published = models.BooleanField(default=True)
    sport_category = models.ForeignKey(SportCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title  

class Description(models.Model):
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    address = models.OneToOneField(Address, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.description  
    
