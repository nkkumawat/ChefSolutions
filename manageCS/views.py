from django.shortcuts import render, redirect
from customer.models import Customers
from order.models import Orders
from cart.models import Cart
# Create your views here.



def manageOrders(request):
    if 'customer_id' in request.session:
        customer = Customers.objects.filter(id = request.session['customer_id'])[0]
        if customer.is_admin:
           data = {}
           data['orders'] = Orders.objects.all()

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
           print(order)
           data['order'] = order
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