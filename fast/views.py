from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product

def home(request):
    products = Product.objects.filter(is_available=True).order_by('-id')[:6]
    context = {
        'products': products
    }
    return render(request, 'home.html', context)


# def about(request):
#     return render(request, 'about.html')