from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def products(request):
    # products = ["iphone", "imac", "ipad"]
    products = Products.objects.all()  #so this is use to derive data from database
    context = {
       'products' :products
    }
    # return HttpResponse(products)
    return render(request, 'myapp/index.html', context)

def product_detail(request, id):
    pro = Products.objects.get(id=id)  # to get a single product
    context = {
        'product': pro
    }
    return render(request, 'myapp/detail.html', context)

def add_product(request):
    if request.method =='POST':
       name = request.POST.get('name')
       price = request.POST.get('price')
       description = request.POST.get('desc')
       image =request.FILES['upload']
       product = Products(name=name, price=price, desc=description,image=image)
       product.save()
    return render(request, 'myapp/addproduct.html')

