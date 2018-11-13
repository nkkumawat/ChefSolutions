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
