from django.urls import path
from .views import get_products, product_detail, search, get_cat_products

urlpatterns = [
   path('', get_products, name= 'get_products'),
   path('<int:id>/', product_detail, name='product_detail'),
   path('search/', search, name='search'),
   path('categories/([a-z]+)', get_cat_products, name="categories"),
   ]