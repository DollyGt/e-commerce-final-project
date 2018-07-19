from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import HttpResponse


# Create your views here.
def get_products(request):
    items = Product.objects.all()
    return render(request, "products/products.html", {'items': items})
    
def product_detail(request, id):
    items = get_object_or_404(Product, id=id)
    return render(request, "products/productdetails.html",{'items': items})
    
def search(request):
    items = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products/products.html", {"items": items})