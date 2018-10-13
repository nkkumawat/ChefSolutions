from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Recipes
from customer.models import Customers
import getResponses
# Create your views here.

data= {}
def addRecipe(request):
    if 'customer_id' in request.session:
        data = getResponses.getResponse(request)
        if request.method == 'POST':
            recipe = Recipes()
            recipe.customer_id = Customers.objects.filter(id=request.session['customer_id'])[0]
            recipe.name = request.POST['name']
            recipe.food_group = request.POST['food_group']
            recipe.no_of_portions = request.POST['no_of_portions']
            recipe.use_of_goods = request.POST['use_of_goods']
            recipe.ingredients = request.POST['ingredients']
            recipe.cooking_process_name = request.POST['cooking_process_name']
            recipe.cooking_process_method = request.POST['cooking_process_method']
            recipe.tags = request.POST['tags']
            recipe.picture_1 = request.FILES['picture_1']
            recipe.picture_2 = request.FILES['picture_2']
            recipe.picture_3 = request.FILES['picture_3']
            recipe.save()
            return render(request , 'blog/sentforapporval.html' , data)
        else:
            return render(request , 'blog/addrecipe.html', data)
    else:
        return HttpResponseRedirect('/customer/login')

def recipes(request):
    data = {}
    if 'customer_id' in request.session:
        data = getResponses.getResponse(request)
    data['recipes'] = Recipes.objects.filter(is_apporved=True)
    return render(request, 'blog/recipes.html', data)