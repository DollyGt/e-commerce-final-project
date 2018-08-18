from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import HttpResponse
from reviews.forms import ReviewForm
from reviews.models import Review
from categories.models import Category

# Create your views here.
def get_products(request):
    items = Product.objects.all()
    return render(request, "products/products.html", {'items': items})
    
def get_cat_products(request, id):
    cat = get_object_or_404(Category, id=id)
    items = cat.products.all()
    return render(request, 'products/products.html', {'items': items})
    
def product_detail(request, id):
    items = get_object_or_404(Product, id=id)
    form=ReviewForm()
    return render(request, "products/productdetails.html",{'items': items, 'review_form': form} )
    
def search(request):
    items = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products/products.html", {"items": items})