from django.shortcuts import render, redirect
from .models import Cart
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from products.models import Products
from django.utils.crypto import get_random_string
from django.db.models import Sum
import getResponses
from coupon.models import CouponCodes

def cart(request):
    data = {}
    data['title'] = "Cart | ChefSolutions"
    data = getResponses.getResponse(request)
    if 'customer_id' in request.session:
        cart = Cart.objects.filter(
            customer_id=request.session['customer_id'], is_purchased=False)
        total_price = 0.0
        for ca in cart:
            total_price += ca.quantity * ca.product_id.price

        data['subtotal'] = total_price
        data['cart'] = cart
        if "coupon_code_id" in request.session:
            # print(request.session['coupon_code_id'])
            coupon = CouponCodes.objects.filter(id=request.session['coupon_code_id'])
            if coupon:
                if total_price >= coupon[0].price_value:
                    data['discount'] = coupon[0].price_value
                else:
                    data['discount']= total_price
                data['coupon_code_id'] = coupon[0].id
                total_price -= data['discount']
        data['total'] = total_price
        return render(request, "cart/cart.html", data)
    elif 'temp_customer_id' in request.session:
        products = []
        cart = Cart.objects.filter(
            temp_customer_id=request.session['temp_customer_id'], is_purchased=False)
        # for c in cart:
        #     product = Products.objects.filter(id=c.product_id.id)
        #     if product[0]:
        #         products.append({"product": product[0], "cart_id": c.id})
        # data['products'] = products
        data["cart"] = cart
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
        if request.method == 'POST':
            if 'temp_customer_id' not in request.session:
                request.session['temp_customer_id'] = get_random_string(
                    length=200)
            product_id = request.POST['product_id']
            temp_customer_id = request.session['temp_customer_id']
            quantity = request.POST['quantity']

            existing_product_cart = Cart.objects.filter(
                temp_customer_id=temp_customer_id,
                product_id=Products.objects.filter(id=product_id)[0],
                is_purchased=False
            )

            if existing_product_cart:
                total = existing_product_cart[0].quantity + int(quantity)
                existing_product_cart.update(
                    quantity=total
                )
            else:
                cart = Cart()
                cart.temp_customer_id = temp_customer_id
                cart.product_id = Products.objects.filter(id=product_id)[0]
                cart.quantity = quantity
                cart.save()

            data = {}
            data['success'] = "true"
            data['added_count'] = Cart.objects.filter(
                temp_customer_id=request.session['temp_customer_id'],
                is_purchased=False
            ).aggregate(total=Sum('quantity'))['total']

            return JsonResponse(data)

    data = getResponses.getResponse(request)
    data['success'] = "false"
    data['added_count'] = 0
    return JsonResponse(data)


def deleteCart(request):

    if 'customer_id' in request.session:
        if request.method == 'POST':
            cart_id = request.POST['cart_id']
            cart = Cart.objects.filter(
                id=cart_id, customer_id=request.session['customer_id'], is_purchased=False)
            if cart:
                cart.delete()
            return redirect("cart:cart")
        else:
            return redirect('error:error')
    else:

        if 'temp_customer_id' not in request.session:
            return redirect('error:error')

        if request.method == 'POST':
            cart_id = request.POST['cart_id']
            cart = Cart.objects.filter(
                id=cart_id,
                temp_customer_id=request.session['temp_customer_id']
            )
            if cart:
                cart.delete()
            return redirect("cart:cart")
        else:
            return redirect('error:error')

def clearCart(request):
    if 'customer_id' in request.session:
        cart = Cart.objects.filter(customer_id=request.session['customer_id'], is_purchased=False)
        if cart:
            cart.delete()
        return redirect("cart:cart")
    else:
        if 'temp_customer_id' not in request.session:
            return redirect('error:error')
        cart = Cart.objects.filter(temp_customer_id=request.session['temp_customer_id'],is_purchased=False  )
        if cart:
            cart.delete()
        return redirect("cart:cart")
