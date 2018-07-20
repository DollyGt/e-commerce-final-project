from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseForbidden
from .forms import ReviewForm
from products.models import Product

# Create your views here.
def add_a_review(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    
    id = int(request.POST['item'])
    items = get_object_or_404(Product, id=id)
    
    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.reviewer = request.user
        review.product = product
        review.save()

    return redirect(reverse('product_detail', args=(id,)))

