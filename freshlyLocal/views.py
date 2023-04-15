from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def say_hello(request):
    
    return render(request, 'hello.html', {'name': 'Mosh'})


def store(request):
    products = Products.objects.all()
    context = {"products" :products}
    return render(request, 'store/store.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
