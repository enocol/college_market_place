from django.shortcuts import render
#from django.views import generic
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
