from django.shortcuts import render, redirect
from .models import Cart
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from products.models import Products
from django.utils.crypto import get_random_string
from django.db.models import Sum


def cart(request):
    data = {}
    data['title'] = "Cart | ChefSolutions"
    if 'customer_id' in request.session:
        cart = Cart.objects.filter(
            customer_id=request.session['customer_id'], is_purchased=False)
        data['cart'] = cart
        return render(request, "cart/cart.html", data)
    elif 'temp_customer_id' in request.session:
        products = []
        cart = Cart.objects.filter(
            temp_customer_id=request.session['temp_customer_id'], is_purchased=False)
        for id in cart:
            product = Products.objects.filter(id=id.product_id)
            if product[0]:
                products.append({"product": product[0], "cart_id": id.id})
        data['products'] = products
        return render(request, "cart/cart.html", data)
    else:
        return render(request, "cart/cart.html")


def addInCart(request):
    if 'customer_id' in request.session:
        if request.method == 'POST':
            product_id = request.POST['product_id']
            customer_id = request.session['customer_id']
            quantity = request.POST['quantity']
            is_present = Cart.objects.filter(customer_id=request.session['customer_id'], product_id=Products.objects.filter(
                id=product_id)[0], is_purchased=False)
            if is_present:
                is_present.update(
                    quantity=is_present[0].quantity + int(quantity))
            else:
                cart = Cart()
                cart.customer_id = customer_id
                cart.product_id = Products.objects.filter(id=product_id)[0]
                cart.quantity = quantity
                cart.save()
            data = {}
            data['success'] = "true"
            data['added_count'] = Cart.objects.filter(
                customer_id=request.session['customer_id'], is_purchased=False).aggregate(total=Sum('quantity'))['total']
            return JsonResponse(data)
        else:
            return HttpResponseRedirect('/error')
    else:
        request.session['temp_customer_id'] = get_random_string(length=200)
        if request.method == 'POST':
            product_id = request.POST['product_id']
            temp_customer_id = request.session['temp_customer_id']
            quantity = request.POST['quantity']
            cart = Cart()
            cart.temp_customer_id = temp_customer_id
            cart.product_id = product_id
            cart.quantity = quantity
            cart.save()
            return HttpResponseRedirect("/cart")
        else:
            return HttpResponseRedirect('/error')


def deleteCart(request):
    if 'customer_id' in request.session:
        if request.method == 'POST':
            cart_id = request.POST['cart_id']
            cart = Cart.objects.filter(
                id=cart_id, customer_id=request.session['customer_id'])
            if cart:
                cart.update(is_purchased=True)
            return HttpResponseRedirect("/cart")
        else:
            return HttpResponseRedirect('/error')
    else:
        request.session['temp_customer_id'] = get_random_string(length=200)
        if request.method == 'POST':
            cart_id = request.POST['cart_id']
            cart = Cart.objects.filter(
                id=cart_id, temp_customer_id=request.session['temp_customer_id'])
            if cart:
                cart.delete()
            return HttpResponseRedirect("/cart")
        else:
            return HttpResponseRedirect('/error')
