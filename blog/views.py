from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Recipes
from customer.models import Customers
import getResponses
import reportlab
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from io import BytesIO
from django.core.files import File
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
            return render(request, 'blog/sentforapporval.html', data)
        else:
            return render(request, 'blog/addrecipe.html', data)
    else:
        return redirect('customer:login')


def recipes(request):
    data = {}
    if 'customer_id' in request.session:
        data = getResponses.getResponse(request)
    data['recipes'] = Recipes.objects.filter(is_apporved=True)
    return render(request, 'blog/recipes.html', data)


def render_to_pdf(path , params ={}):
    template = get_template(path)
    html = template.render(params)
    response = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
    if not pdf.err:
        return HttpResponse(response.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse("Error Rendering PDF", status=400)

def printRecipe(request, rid):
    recipe = Recipes.objects.filter(id= rid,is_apporved=True)
    if recipe.__len__():
        pdf = render_to_pdf('blog/printtemplate.html', {'data' : recipe})
        return HttpResponse(pdf, content_type='application/pdf')
    else:
        return redirect('error:error')
