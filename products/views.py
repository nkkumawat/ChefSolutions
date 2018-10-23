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
        products = Products.objects.filter(category=request.GET['category'])
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
