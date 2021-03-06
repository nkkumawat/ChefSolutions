from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from .models import Recipes, Comments
from customer.models import Customers
import getResponses
from products.models import Products
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.

data = {}


def addRecipe(request):

    if 'customer_id' in request.session:
        data = getResponses.getResponse(request)
        if request.method == 'POST':
            recipe = Recipes()
            recipe.customer_id = Customers.objects.filter(
                id=request.session['customer_id'])[0]
            recipe.name = request.POST['name']
            recipe.food_group = request.POST['food_group']
            product_ids = request.POST.getlist('use_of_products')
            recipe.use_of_products = ""
            for id in product_ids:
                recipe.use_of_products += id + "$"
            recipe.ingredients = request.POST['ingredients']
            recipe.cooking_process_name = request.POST['cooking_process_name']
            recipe.cooking_process_method = request.POST['cooking_process_method']
            recipe.tags = request.POST['tags']
            recipe.video_url = request.POST['video_url']

            if 'picture_1' in request.FILES:
                recipe.picture_1 = request.FILES['picture_1']

            if 'picture_2' in request.FILES:
                recipe.picture_2 = request.FILES['picture_2']

            if 'picture_3' in request.FILES:
                recipe.picture_3 = request.FILES['picture_3']

            recipe.save()
            return render(request, 'blog/sentforapporval.html', data)
        else:
            products = Products.objects.all()
            data['products'] = products
            return render(request, 'blog/addrecipe.html', data)
    else:
        return redirect('customer:login')


def recipes(request):
    data = {}
    if 'customer_id' in request.session:
        data = getResponses.getResponse(request)
    data['recipes'] = Recipes.objects.filter(is_apporved=True)

    def ratingSystem(elem):
        return elem.total_rating

    topRecipes = sorted(data['recipes'], key=ratingSystem, reverse=True)

    if len(topRecipes) > 5:
        data['top_rated'] = topRecipes[0:5]
    else:
        data['top_rated'] = topRecipes

    for i in range(0, len(data['recipes'])):
        data['recipes'][i].use_of_products = data['recipes'][i].use_of_products.split('$')[
            :-1]

    return render(request, 'blog/recipes.html', data)


def recipesDetail(request, id):
    data = {}
    if 'customer_id' in request.session:
        data = getResponses.getResponse(request)
    data['recipes'] = Recipes.objects.get(id=id)

    def ratingSystem(elem):
        return elem.total_rating

    topRecipes = sorted(Recipes.objects.filter(
        is_apporved=True), key=ratingSystem, reverse=True)

    if len(topRecipes) > 5:
        data['top_rated'] = topRecipes[0:5]
    else:
        data['top_rated'] = topRecipes

    data['recipes'].use_of_products = data['recipes'].use_of_products.split('$')[
        :-1]

    products = []
    for idx in data['recipes'].use_of_products:
        if idx != '':
            product = Products.objects.filter(id=idx)[0]
            products.insert(0, product)
    data['products'] = products

    data['comments'] = Comments.objects.filter(recipe=data['recipes'])

    return render(request, 'blog/recipesDetail.html', data)


def render_to_pdf(path, params={}):
    template = get_template(path)
    html = template.render(params)
    response = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
    if not pdf.err:
        return HttpResponse(response.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse("Error Rendering PDF", status=400)


def printRecipe(request, rid):
    recipe = Recipes.objects.filter(id=rid, is_apporved=True)
    if recipe.__len__():
        pdf = render_to_pdf('blog/printtemplate.html', {'data': recipe})
        return HttpResponse(pdf, content_type='application/pdf')
    else:
        return redirect('error:error')


def addComment(request):
    if request.method == 'GET':
        return redirect('error:error')

    elif request.method == 'POST':
        customer = Customers.objects.get(id=request.POST['customerId'])
        recipe = Recipes.objects.get(id=request.POST['recipeId'])
        comment = Comments(
            text=request.POST['text'], user=customer, recipe=recipe)
        comment.save()
        return JsonResponse(data={'success': True, 'comment': comment.text})
