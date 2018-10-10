from django.shortcuts import render
from .models import Cart
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

data = {
    "title":"chef solutions",
    "message": ""
}

def cart(request):
    if 'customer_id' in request.session:
        result = []
        product_ids = Cart.objects.filter(customer_id=request.session['customer_id'], is_purchased=False)
        for id in product_ids:
            result.append(id)
        data['result'] = result
        return render(request, "cart/cart.html", data)
    else:
        return HttpResponseRedirect("/error")


def addInCart(request):
    if 'customer_id' in request.session:
        if request.method =='POST':
            product_id = request.POST['product_id']
            customer_id = request.session['customer_id']
            quantity = request.POST['quantity']
            cart = Cart()
            cart.customer_id = customer_id
            cart.product_id = product_id
            cart.quantity = quantity
            cart.save()
            return HttpResponseRedirect("/cart")
        else:
            return HttpResponseRedirect('/error')
    else:
        return HttpResponseRedirect("/customer/login")