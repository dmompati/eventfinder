from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    # start_time = models.DateTimeField('start time and date')
    # end_time = models.DateTimeField('end time and date')

    def __str__(self):
        return self.title



class Category(models.Model):
    name = models.CharField(max_length=50)
    
   
class Users(models.Model):
   category_id = models.CharField(max_length=50)
   name = models.CharField(max_length=50)