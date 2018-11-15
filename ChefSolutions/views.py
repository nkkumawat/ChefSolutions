from django.shortcuts import render
from blog.models import Recipes
from products.models import Products
import getResponses


def homepage(request):
    data = getResponses.getResponse(request)
    data['recipes'] = Recipes.objects.order_by('-add_date')[:6]
    data['products'] = Products.objects.order_by('added_date')[:6]
    return render(request, 'base/index.html', data)


def aboutus(request):
    return render(request, 'base/aboutus.html')


def search(request):
    data = {}
    if request.method == 'GET':
        item = request.GET['item']

        data['product'] = {}

        productName = Products.objects.filter(name__icontains=item)
        productDescription = Products.objects.filter(description__icontains=item)
        productUses = Products.objects.filter(uses__icontains=item)
        productBenefits = Products.objects.filter(benefits__icontains=item)
        productIngridients = Products.objects.filter(ingridients__icontains=item)
        productDirection = Products.objects.filter(directions__icontains=item)

        def productJson(obj, name):
            if len(obj) != 0:
                data['product'][name] = obj

        productJson(productName, 'productName')
        productJson(productDescription, 'productDescription')
        productJson(productUses, 'productUses')
        productJson(productBenefits, 'productBenefits')
        productJson(productIngridients, 'productIngridients')
        productJson(productDirection, 'productDirection')

        print(data)

    return render(request, 'base/search.html', data)
