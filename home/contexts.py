from categories.models import Category

def get_menu_items():
    all_items = Category.objects.all()
    return all_items