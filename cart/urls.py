from django.urls import path
from .views import view_cart, add_to_cart, remove_item


urlpatterns=[
    path('cart/view', view_cart, name='view_cart'),
    path('cart/add', add_to_cart, name='add_to_cart'),
    path('cart/remove', remove_item, name='remove_item'),
    ]
    
