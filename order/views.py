from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from cart.models import Cart
from products.models import Products

from django.db.models import Sum


def placeOrder(request):
    data = {}
    data['title'] = "Order | Chef Solutions"
    if 'customer_id' in request.session:
        products = []
        total_ammount = 0.0
        cart = Cart.objects.filter(customer_id=request.session['customer_id'], is_purchased=False)
        for id in cart:
            product = Products.objects.filter(id=id.product_id)
            count = product.aggregate(total = Sum('price'))
            print(count['total'])
            total_ammount += count['total']
            if product[0]:
                products.append({"product": product[0], "cart_id": id.id})
        data['products'] = products
        data['total_ammount'] = total_ammount
        return render(request , 'order/placeorder.html' , data)

    else:
        return HttpResponseRedirect('/customer/login')