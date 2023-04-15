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
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Orders.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []

    context = {'items':items}
    return render(request, 'store/cart.html', context)


def checkout(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Orders.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items =[]
        order = {'get_cart_total':0,'get_cart_item':0}
    context = {'item':items, 'order':order}
    return render(request, 'store/checkout.html', context)
