from django.shortcuts import render
from .models import Products
# Create your views here.

data = {
    "title" : "Products | Chef solutions",
    "message": ""
}
def allProducts(request):
    products = Products.objects.all()
    data['products'] = products
    return render(request, "products/products.html", data)


def prductDetail(request,pid):
    product = Products.objects.filter(id=pid)
    if product:
        print(product)
        data['product'] = product
        return render(request, "products/productdetails.html", data)
    else:
        return render(request, "error.html" )
