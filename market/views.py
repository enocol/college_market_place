from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product
from .form import Form

# Create your views here.
def index(request):
    product = Product.objects.all()
    context = {'products': product}
    messages.success(request, '')
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

def form(request):
    form = Form(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            form.save()
            message = 'Product added successfully'
            return render(request, 'market/confirmation.html', {'message': message})
    else:
        form = Form()   


    return render(request, 'market/add_item.html', {'form': form})


def edit_product(request, id):
    product = Product.objects.get(id=id)
    form = Form(request.POST or None, request.FILES or None,  instance=product)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'market/edit_product.html', {'form': form, 'product': product})