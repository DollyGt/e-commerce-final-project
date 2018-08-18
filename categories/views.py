from django.shortcuts import render

# Create your views here.
def get_cats(request):
    items = Category.objects.all()
    return items