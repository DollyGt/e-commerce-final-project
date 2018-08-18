from django.db import models
from categories.models import Category

def categories(request):
    return {
        'categories': Category.objects.all()
    }