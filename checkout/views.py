from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import OrderForm, MakePaymentForm
from products.models import Product
from .models import OrderLineItem
from django.conf import settings
from cart.utils import get_cart_items_and_total

# Create your views here.

def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save()
            
            cart = request.session.get('cart', {})
            for product_id, quantity in cart.items():
                line_item = OrderLineItem()
                line_item.order = order
                
                line_item.product = get_object_or_404(Product, pk=product_id)
                line_item.quantity = quantity
                line_item.save()
        
        
            del request.session['cart']
        return HttpResponse("Order made successfully!")
    else:
        order_form = OrderForm()
        payment_form = MakePaymentForm()
        context = {'order_form': order_form, 'payment_form': payment_form }
        cart = request.session.get('cart', {})
        cart_items_and_total = get_cart_items_and_total(cart)
        context.update(cart_items_and_total)
        
        return render(request, "checkout/checkout.html", context)