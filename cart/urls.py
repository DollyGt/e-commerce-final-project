from django.urls import path
from .views import view_cart, add_to_cart, update_cart, buynow, remove_from_cart


urlpatterns=[
    path('view/', view_cart, name='view_cart'),
    path('add/', add_to_cart, name='add_to_cart'),
    path('update_cart/', update_cart, name='update_cart'),
    path('remove_from_cart/', remove_from_cart, name='remove_from_cart'),
    path('buynow/', buynow, name='buynow'),
    ]
    
