from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseForbidden
from .forms import ReviewForm
from products.models import Product

# Create your views here.
def add_a_review(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    
    product_id = int(request.POST['product'])
    items = get_object_or_404(Product, pk=product_id)
    
    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.reviewer = request.user
        review.items = items
        review.save()

    return redirect(reverse('product_detail', args=(product_id,)))

