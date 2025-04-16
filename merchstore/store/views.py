from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import *

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    productTypes = ProductType.objects.all()
    ctx = {
        'products':products,
        'productTypes':productTypes
    }
    return render(request,'product_list.html',ctx)

def product_detail(request, num=1):
    product = Product.objects.get(pk=num)
    ctx = {
        'product':product,
    }
    return render(request,'product_detail.html',ctx)

def product_create(request):
    pass

def product_update(request):
    pass

def cart(request):
    pass

def transactions(request):
    pass


