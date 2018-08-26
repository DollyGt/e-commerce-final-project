from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from products.models import Product
from .utils import get_cart_items_and_total
from django.contrib import messages

# Create your views here.


def view_cart(request):
    cart = request.session.get('cart', {})
    context = get_cart_items_and_total(cart)
    return render(request, "cart/cart.html", context)
  
def add_to_cart(request):

    # Get the product we're adding
    id = request.POST['product_id']
    quantity = int(request.POST['quantity'])
    items = get_object_or_404(Product, pk=id)
    
    # Get the current Cart
    cart = request.session.get('cart', {})
    
    # Update the Cart
    cart[id] = cart.get(id, 0) + quantity
    
    # Save the Cart back to the session
    request.session['cart'] = cart
    msg = "%s is added to cart."% items.name
    messages.error(request, msg)
    # Redirect somewhere
    return redirect('get_products')
    

def remove_from_cart(request): 
    id = request.POST['product_id']
    products = get_object_or_404(Product, pk=id)
    cart = request.session.get('cart', {})
    del cart[id]
    request.session['cart'] = cart
    messages.error(request, "Your item is removed from your cart.")
    return redirect('view_cart')

def update_cart(request): 
    id = request.POST['product_id']
    quantity = int(request.POST['quantity'])
    products = get_object_or_404(Product, pk=id)
    cart = request.session.get('cart', {})
    
    cart[id] = cart.get(id, 0 ) * 0 + quantity
    
    request.session['cart'] = cart
    messages.error(request, "Your cart is updated.")
    return redirect('view_cart')    

def buynow(request):

    # Get the product we're adding
    id = request.POST['product_id']
    items = get_object_or_404(Product, pk=id)
    
    # Get the current Cart
    cart = request.session.get('cart', {})
    
    # Update the Cart
    cart[id] = cart.get(id, 0) + 1
    
    # Save the Cart back to the session
    request.session['cart'] = cart
    
    # Redirect somewhere
    return redirect('view_cart')