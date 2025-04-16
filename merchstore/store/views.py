from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import *

# Create your views here.

def product_list(request):
    productTypes = ProductType.objects.all()

    if request.user.is_authenticated:
        products = Product.objects.exclude(owner=request.user.profile)
        user_products = Product.objects.filter(owner=request.user.profile)

    else:
        products = Product.objects.all()
        user_products = Product.objects.none()
        
    ctx = {
        'products':products,
        'productTypes':productTypes,
        'user_products' : user_products
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


