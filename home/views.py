from django.shortcuts import render

from django.db.models import Q

# Create your views here.
def get_index(request):
    return render(request, "index.html")

def search(request):
    template ='index.html'
    
    query = request.GET.get('q')
    
    results = Post.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
    
    pages = pagination(request, results,product.id)
    
    context = {
    'items': pages[0],
    'page_range': pages[1],
    }
    return render(request, "products.html")