from products.models import Product

def get_menu_items(request):
    all_items = Product.objects.all()
    cat_set = list(set([(category.category).lower() for category in all_items]))
    return {'categories': cat_set }