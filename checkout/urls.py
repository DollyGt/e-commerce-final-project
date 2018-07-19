from django.urls import path
from .views import checkout

urlpatterns = [
    path('', checkout, name='checkout'),
    # path('buy/', buy_now, name='buy_now'),
]