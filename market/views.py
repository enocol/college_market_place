from django.shortcuts import render

# Create your views here.
def index(request):
    product = Product.objects.all()
    context = {'product': product}
    return render(request, 'market/index.html', context)