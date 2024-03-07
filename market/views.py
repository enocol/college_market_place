from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product

# Create your views here.
def index(request):
    product = Product.objects.all()
    context = {'products': product}
    return render(request, 'market/index.html', context)


def product_detail(request, id):
    product = Product.objects.get(id=id)
    context = { 
        'product': product
    }
    return render(request, 'market/product_detail.html', context)


def about(request):
    return render(request, 'market/about.html')


def delete_product(request, id):
    product = Product.objects.filter(id=id)
    product.delete()
    message = 'Product deleted successfully'
    context = {'message': message,
               'product': product}

    return render(request, 'market/delete.html', context)