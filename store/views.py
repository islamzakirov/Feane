from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
def store(request, category_slug=None):
   
    if category_slug == None:
        products = Product.objects.filter(is_available=True)
    else:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(is_available=True, category=categories)

    paginator = Paginator(products, 3)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    context = {
        'products': paged_products,
        'products_count': products.count()
    }
    print("============")
    
    return render(request, 'store.html', context)

def product_detail(request, category_slug, product_slug):
    return render(request, 'product_detail.html')

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET.get('keyword')
    if keyword:
        products = Product.objects.filter(Q(name__icontains=keyword) | Q(description__icontains=keyword))
    
    context = {
        'products': products,
        'product_count': products.count()
    }
    return render(request, 'store.html', context)