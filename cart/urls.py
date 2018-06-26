from django.urls import path
from.views import view_cart
from.views import add_to_cart

urlpatterns=[
    path('cart/view', view_cart, name='view_cart'),
    path('cart/add', add_to_cart, name='add_to_cart'),
    ]