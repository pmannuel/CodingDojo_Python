from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import Products

def index(request):
    data = {
        "products" : Products.objects.all()
    }
    return render(request,'srr/index.html', data)

def show(request, product_id):
    data = {
        "show_product" : Products.objects.get(id = product_id)
    }
    return render(request,'srr/show.html', data)

def edit(request, product_id):
    data = {
        "edit_product" : Products.objects.get(id = product_id)
    }

    return render(request,'srr/edit.html', data)

def save_edit(request, product_id):
    if request.method == "POST":
        edit_product = Products.objects.filter(id = product_id)
        edit_product.update(
            name = request.POST['name'],
            description = request.POST['description'],
            price = request.POST['price']
        )

    return redirect(reverse('srr:index'))

def remove(request, product_id):
    Products.objects.get(id = product_id).delete()

    return redirect(reverse('srr:index'))

def addprod(request):
    if request.method == "POST":
        Products.objects.create(
            name = request.POST['name'],
            description = request.POST['description'],
            price = request.POST['price']
        )

    return render(request,'srr/addprod.html')
