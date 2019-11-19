from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse, path


class Event(models.Model):
    title = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    # start_time = models.DateTimeField('start time and date')
    # end_time = models.DateTimeField('end time and date')

    def __str__(self): 
        return self.title

    def get_absolute_url(self):
        return reverse('<pk>')


class Category(models.Model):
    name = models.CharField(max_length=50)
    
   
class Users(models.Model):
   category_id = models.CharField(max_length=50)
   name = models.CharField(max_length=50)