from django.shortcuts import render, HttpResponse
from product.models import Product

def home(request):
    products = Product.objects.all().filter(is_available=True)
    context = {
        'products': products,
        'title': 'One of the Biggest Online Shopping Platform',
    }
    return render(request, 'home.html', context)

def welcome(request):
    return HttpResponse('Welcome to Python')
