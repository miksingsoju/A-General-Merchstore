from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import *

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    ctx = {
        'products':products
    }
    return render(request,'product_list.html',ctx)

def product_detail(request, num):
    pass

def product_create(request):
    pass

def product_update(request):
    pass

def cart(request):
    pass

def transactions(request):
    pass


