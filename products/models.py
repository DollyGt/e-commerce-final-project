from django.db import models
from django.db.models import Avg
from decimal import Decimal

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    priceOld = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal('0.00'))
    image = models.ImageField(upload_to='images')
    featured = models.BooleanField(default=False)

    @property
    def discount(self):
        if self.priceOld > self.price:
            discount = self.price * 100 / self.priceOld
            return round(discount)
        else:
            return 0
    
    @property
    def average_rating(self):
        if self.reviews_received.all():
            average = self.reviews_received.all().aggregate(Avg('rating'))
            n = average['rating__avg']
            return float(round(n, 2))
        else:
            return 0
        
    @property
    def stars(self):
        return range(int(self.average_rating))
        
    @property 
    def needs_half_star(self):
        remainder = self.average_rating - int(self.average_rating)
        return 0.4 < remainder
    
    
    def __str__(self):
        return self.name