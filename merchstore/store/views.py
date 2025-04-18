from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

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
    images = ProductImage.objects.filter(product__exact=product)
    ctx = {
        'product':product,
        'images': images
    }
    return render(request,'product_detail.html',ctx)

@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user.profile  # set owner manually
            product.save()
            return redirect('store:product_detail', product.id)
    else:
        form = ProductForm()

    return render(request, 'product_create.html', {'form': form})

@login_required
def product_update(request,num):
    product = Product.objects.get(id=num)

    # Ensure that the form is being submitted via POST
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            # Automatically set the product status based on stock
            product = form.save(commit=False)
            if product.stock == 0:
                product.status = 'Out of Stock'
            else:
                product.status = 'Available'
            product.save()

            return redirect('store:product_detail', num=product.id)
    else:
        form = ProductForm(instance=product)

    return render(request, 'product_update.html', {'form': form})

def cart(request):
    pass

def transactions(request):
    pass


