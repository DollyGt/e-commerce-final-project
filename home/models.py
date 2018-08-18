from django.db import models
from categories.models import Category

# Create your models here.

class Home(models.Model):
    name = 'ffghh'
        
    @property 
    def some(self):
        string = 'some string testing'
        return string
        
    def __str__(self):
        return self.name