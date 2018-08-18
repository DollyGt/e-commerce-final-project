from django.db import models
from products.models import Product

class Category(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    products = models.ManyToManyField(Product, related_name='products')
    
    @property
    def get_all(self):
        cats = self.objects.all()
        return cats

    def __str__(self):
        return self.name    

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']
   
