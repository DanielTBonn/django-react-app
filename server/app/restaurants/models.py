from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)
    restaurants = models.ManyToManyField(Restaurant)

    def __str__(self):
        return self.name 
    
class Dish(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    restaurant = models.ForeignKey(Restaurant, 
                                   on_delete=models.CASCADE)

    def __str__(self):
        return self.name
