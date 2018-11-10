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
        if  request.GET['category'] == 'is_vegetarian':
            products = Products.objects.filter(is_vegetarian=True)
        elif request.GET['category'] == 'low_salt':
            products = Products.objects.filter(low_salt = True)
        elif request.GET['category'] == 'no_added_msg':
            products = Products.objects.filter(added_msg=True)
        elif request.GET['category'] == 'built_in_tenderizer':
            products = Products.objects.filter(built_in_tenderizer=True)
        elif request.GET['category'] == 'multi_application':
            products = Products.objects.filter(multi_application=True)
        elif request.GET['category'] == 'three_in_one':
            products = Products.objects.filter(three_in_one=True)
        elif request.GET['category'] == 'easy_to_use':
            products = Products.objects.filter(easy_to_use=True)
        elif request.GET['category'] == 'egg_free':
            products = Products.objects.filter(egg_free=True)
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
    data = getResponses.getResponse(request)
    if product:
        print(product)
        data['product'] = product[0]
        return render(request, "products/productdetails.html", data)
    else:
        return redirect('error:error')


