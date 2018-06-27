from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from products.models import Product

# Create your views here.
def view_cart(request):
    cart = request.session.get('cart', {})
    cart_total = 0
    cart_items = []
    
    for p in cart:
        phone = get_object_or_404(Product, pk=p)
        quantity = cart[p]
        
        cart_item = {
            'product': phone,
            # 'image': product.image,
            'quantity': quantity,
            # 'price': product.price,
            'sub_total': phone.price * quantity
        }
        cart_items.append(cart_item)
        cart_total += cart_item['sub_total']
        

    return render(request, "cart/cart.html", {'cart_items': cart_items, 'cart_total': cart_total})

    
def add_to_cart(request):

    # Get the product we're adding
    id = request.POST['product_id']
    phone = get_object_or_404(Product, pk=id)
    
    # Get the current Cart
    cart = request.session.get('cart', {})
    
    # Update the Cart
    cart[id] = cart.get(id, 0) + 1
    
    # Save the Cart back to the session
    request.session['cart'] = cart
    
    # Redirect somewhere
    return HttpResponse(cart[id])
    
def remove_item(request): 
    id = request.POST['product_id']
    products = get_object_or_404(Product, pk=id)
    cart = request.session.get('cart', {})
    del cart[id]
    request.session['cart'] = cart
    return redirect('view_cart')
