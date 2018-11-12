from django.http import HttpResponse
from django.shortcuts import render, redirect
from customer.models import Customers , Address, RequestForB2B
from order.models import Orders
from cart.models import Cart
from products.models import Products
from blog.views import render_to_pdf
from blog.models import Recipes
import getResponses

# Create your views here.



def manageOrders(request):

    if 'customer_id' in request.session:
        customer = Customers.objects.filter(id = request.session['customer_id'])[0]
        if customer.is_admin:
           data = {}
           data = getResponses.getResponse(request)
           data['orders'] = Orders.objects.all().reverse()

           return render(request, "manageCS/orders.html", data)
        else:
            return redirect("error:error")
    else:
        return redirect("error:error")

def manageOrderSingle(request):
    if 'customer_id' in request.session:
        customer = Customers.objects.filter(id = request.session['customer_id'])[0]
        if customer.is_admin:
            data = {}
            data = getResponses.getResponse(request)
            order = Orders.objects.filter(id = request.POST['order_id'])[0]
            address = Address.objects.filter(customer_id=customer)
            data['order'] = order
            data['address'] = address
            cart_ids = order.cart_id
            cart_ids = cart_ids.split("$")
            carts = []
            for id in cart_ids:
               if id != '':
                   cart = Cart.objects.filter(id=id)[0]
                   carts.insert(0,cart)

            data['cart'] = carts

            return render(request, "manageCS/singleorder.html", data)
        else:
            return redirect("error:error")
    else:
        return redirect("error:error")



def manageProducts(request):
    if 'customer_id' in request.session:
        customer = Customers.objects.filter(id = request.session['customer_id'])[0]
        if customer.is_admin:
           data = {}
           data = getResponses.getResponse(request)
           data['products'] = Products.objects.all().reverse()

           return render(request, "manageCS/products.html", data)
        else:
            return redirect("error:error")
    else:
        return redirect("error:error")

def manageProductSingle(request):
    if 'customer_id' in request.session:
        customer = Customers.objects.filter(id = request.session['customer_id'])[0]
        if customer.is_admin:
            data = getResponses.getResponse(request)
            product = Products.objects.filter(id = request.POST['product_id'])[0]
            data['product'] = product
            return render(request, "manageCS/singleproduct.html", data)
        else:
            return redirect("error:error")
    else:
        return redirect("error:error")

def addProduct(request):
    if 'customer_id' in request.session:
        customer = Customers.objects.filter(id = request.session['customer_id'])[0]
        if customer.is_admin:
            if request.method == 'POST':
                data = {}
                data = getResponses.getResponse(request)
                product  = Products()
                product.name = request.POST['name']

                product.price = request.POST['price']
                product.b2b_price = request.POST['b2b_price']
                product.size = request.POST['size']
                product.energy = request.POST['energy']
                product.protein = request.POST['protein']
                product.carbohydrates = request.POST['carbohydrates']
                product.sugar = request.POST['sugar']
                product.fat  = request.POST['fat']
                product.available_qty = request.POST['available_qty']

                product.is_vegetarian =    True if 'is_vegetarian' in request.POST and request.POST['is_vegetarian'] == "on" else  False
                product.added_msg =  True if 'added_msg' in request.POST and request.POST['added_msg'] == "on" else  False
                product.low_salt =  True if 'low_salt' in request.POST and request.POST['low_salt'] == "on" else  False
                product.built_in_tenderizer =  True if 'built_in_tenderizer' in request.POST and request.POST['built_in_tenderizer'] == "on" else  False
                product.multi_application =  True if 'multi_application' in request.POST and request.POST['multi_application'] == "on" else  False
                product.three_in_one =  True if 'three_in_one' in request.POST and request.POST['three_in_one'] == "on" else  False
                product.easy_to_use =  True if 'easy_to_use' in request.POST and request.POST['easy_to_use'] == "on" else  False
                product.egg_free =  True if 'egg_free' in request.POST and request.POST['egg_free'] == "on" else  False
                # print(request.POST['is_vegetarian'])

                product.shelf_life = request.POST['shelf_life']
                product.description = request.POST['description']
                product.storage = request.POST['storage']
                product.uses = request.POST['uses']
                product.benefits = request.POST['benefits']
                product.ingridients = request.POST['ingridients']
                product.directions = request.POST['directions']
                product.category = request.POST['category']
                product.picture_1 = request.FILES['picture_1']
                product.picture_2 = request.FILES['picture_2']
                product.picture_3 = request.FILES['picture_3']
                print(request.POST['category'])
                product.save()
                data['massage'] = "Added"
                return render(request, "manageCS/addproduct.html" ,data)
            else:
                return render(request, "manageCS/addproduct.html")
        else:
            return redirect("error:error")
    else:
        return redirect("error:error")

def deleteProduct(request):
    if 'customer_id' in request.session:
        customer = Customers.objects.filter(id = request.session['customer_id'])[0]
        if customer.is_admin:
            id = request.POST['product_id']
            prodcut = Products.objects.filter(id= id)
            prodcut.delete()
            return redirect("manageCS:manageProducts")
        else:
            return redirect("error:error")
    else:
        return redirect("error:error")



def manageRecipeRequest(request):
    if 'customer_id' in request.session:
        customer = Customers.objects.filter(id=request.session['customer_id'])[0]
        data = {}
        data = getResponses.getResponse(request)
        if customer.is_admin:
            if request.method == 'POST':
                id = request.POST['recipe_id']
                Recipes.objects.filter(id=id).update(is_apporved = True)
            data['requests'] = Recipes.objects.filter(is_apporved=False)
            return render(request , "manageCS/requestrecipe.html" , data)
        else:
            return redirect("error:error")
    else:
        return redirect("error:error")

def manageRecipeRequestSingle(request):
    if 'customer_id' in request.session:
        customer = Customers.objects.filter(id=request.session['customer_id'])[0]
        data = {}
        data = getResponses.getResponse(request)
        if customer.is_admin:
            if request.method == 'POST':
                id = request.POST['recipe_id']
                if 'apporve' in request.POST:
                    Recipes.objects.filter(id=id).update(is_apporved = True)
                    return redirect("manageCS:manageRecipeRequest")
                else:
                    recipe = Recipes.objects.filter(id=id)
                    product_ids = recipe[0].use_of_products.split("$")
                    products = []
                    for idx in product_ids:
                        if idx != '':
                            product = Products.objects.filter(id=idx)[0]
                            products.insert(0, product)
                    data['products'] = products
                    data['recipe'] = recipe[0]

                    return render(request , "manageCS/requestrecipesingle.html" , data)
            else:
                return redirect("error:error")
        else:
            return redirect("error:error")
    else:
        return redirect("error:error")


def manageB2BRequest(request):
    if 'customer_id' in request.session:
        customer = Customers.objects.filter(id=request.session['customer_id'])[0]
        data = {}
        data = getResponses.getResponse(request)
        if customer.is_admin:
            if request.method == 'POST':
                id = request.POST['request_id']
                request_b2b = RequestForB2B.objects.filter(id = id)
                customer = Customers.objects.filter(id=request_b2b[0].customer_id.id)
                customer.update(is_b2b = True)
                request_b2b.update(is_responsed = True)

            data['requests'] = RequestForB2B.objects.all()
            return render(request , "manageCS/requestb2b.html" , data)
        else:
            return redirect("error:error")
    else:
        return redirect("error:error")


def printRecipt(request):
    if 'customer_id' in request.session:
        customer = Customers.objects.filter(id=request.session['customer_id'])[0]

        if customer.is_admin:
            if request.method == 'POST':
                data = {}
                data = getResponses.getResponse(request)
                order = Orders.objects.filter(id=request.POST['order_id'])[0]
                address = Address.objects.filter(customer_id=customer)
                data['order'] = order
                data['address'] = address
                cart_ids = order.cart_id
                cart_ids = cart_ids.split("$")
                carts = []
                for id in cart_ids:
                    if id != '':
                        cart = Cart.objects.filter(id=id)[0]
                        carts.insert(0, cart)

                data['cart'] = carts
                pdf = render_to_pdf('manageCS/recipt.html', data)
                return HttpResponse(pdf, content_type='application/pdf')

                # return render(request , "manageCS/recipt.html" , data)

            else:
                return redirect("error:error")
        else:
            return redirect("error:error")
    else:
        return redirect("error:error")