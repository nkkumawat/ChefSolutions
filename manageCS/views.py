from django.http import HttpResponse
from django.shortcuts import render, redirect
from customer.models import Customers , Address, RequestForB2B
from order.models import Orders
from cart.models import Cart
from products.models import Products
from blog.views import render_to_pdf

# Create your views here.



def manageOrders(request):
    if 'customer_id' in request.session:
        customer = Customers.objects.filter(id = request.session['customer_id'])[0]
        if customer.is_admin:
           data = {}
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
            data = {}
            product = Products.objects.filter(id = request.POST['product_id'])[0]
            data['product'] = product
            print(product)
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

                product.is_vegetarian =    True if request.POST['is_vegetarian'] == "on" else  False
                product.added_msg =  True if request.POST['added_msg'] == "on" else  False
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



def manageB2BRequest(request):
    if 'customer_id' in request.session:
        customer = Customers.objects.filter(id=request.session['customer_id'])[0]
        data = {}
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
        data = {}
        if customer.is_admin:
            if request.method == 'POST':
                data = {}
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