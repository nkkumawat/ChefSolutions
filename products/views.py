from django.shortcuts import render, redirect
from .models import Products
import getResponses
from cart.models import Cart
# Create your views here.

data = {
    "title": "Products | Chef solutions",
    "message": ""
}


def allProducts(request):
    if request.GET['category'] != 'none':
        if  request.GET['category'] == 'vegetarian':
            products = Products.objects.filter(is_vegetarian=True)
        elif request.GET['category'] == 'low_fat':
            products = Products.objects.filter(fat__lte = 5)
        else: # last for low sugar
            products = Products.objects.filter(sugar__lte=5)
    else:
        products = Products.objects.all()

    data = getResponses.getResponse(request)
    data['products'] = products

    allCategories = Products.objects.only('category')
    uniqueCategories = []
    for category in allCategories:
        if category.category not in uniqueCategories:
            uniqueCategories.append(category.category)

    data['categories'] = uniqueCategories
    return render(request, "products/products.html", data)


def prductDetail(request, pid):
    product = Products.objects.filter(id=pid)
    if product:
        print(product)
        data['product'] = product[0]
        return render(request, "products/productdetails.html", data)
    else:
        return redirect('error:error')
