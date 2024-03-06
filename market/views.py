from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    product = Product.objects.all()
    context = {'products': product}
    return render(request, 'market/index.html', context)