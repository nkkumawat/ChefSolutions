from django.shortcuts import render
from .models import Products
import getResponses
from cart.models import Cart
# Create your views here.

data = {
    "title" : "Products | Chef solutions",
    "message": ""
}
def allProducts(request):
    products = Products.objects.all()
    data = getResponses.getResponse(request)
    data['products'] = products



    return render(request, "products/products.html", data)


def prductDetail(request,pid):
    product = Products.objects.filter(id=pid)
    if product:
        print(product)
        data['product'] = product
        return render(request, "products/productdetails.html", data)
    else:
        return render(request, "base/error.html")
