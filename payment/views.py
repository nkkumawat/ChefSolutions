from django.shortcuts import render, reverse

# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import logging
import traceback
import hashlib
from random import randint
from django.views.decorators.csrf import csrf_exempt
from .constants import PAYMENT_URL_TEST, PAID_FEE_PRODUCT_INFO
from .constants import SERVICE_PROVIDER , TEST_MERCHANT_KEY ,TEST_MERCHANT_SALT
from cart.models import Cart
from customer.models import Customers

def payment(request):
    if 'customer_id' in request.session:
        cart_details = Cart.objects.filter(customer_id=request.session['customer_id'], is_purchased=False)
        total_price = 0.0
        for cart in cart_details:
            total_price += cart.quantity * cart.product_id.price

        customer = Customers.objects.filter(id=request.session['customer_id'])[0]
        # print(customer.name)
        data = {}
        txnid = get_transaction_id()
        hash = generate_hash(request, txnid,total_price, customer.name.split(" ")[0], customer.email)
        # hash_string = get_hash_string(request, txnid, total_price, customer.name, customer.email)

        # use test URL for testing
        data["action"] = PAYMENT_URL_TEST
        data["amount"] = float(total_price)
        data["productinfo"] = "info"
        data["key"] = TEST_MERCHANT_KEY
        data["txnid"] = txnid
        data["hash"] = hash
        data["firstname"] = customer.name.split(" ")[0]
        data["email"] = customer.email
        data["phone"] = customer.mobile
        data["service_provider"] = SERVICE_PROVIDER
        data["furl"] = request.build_absolute_uri(reverse("payment:payment_failure"))
        data["surl"] = request.build_absolute_uri(reverse("payment:payment_success"))
        return render(request, "payment/payment.html", data)
    else:
         return redirect('error:error')



# generate the hash
def generate_hash(request, txnid , total_price, name, email):
    try:
        hash_string = get_hash_string(request, txnid, total_price, name, email)
        generated_hash = hashlib.sha512(
            hash_string.encode('utf-8')).hexdigest().lower()
        return generated_hash
    except Exception as e:
        print(e)
        return None

def get_hash_string(request, txnid , total_price, name, email):
    hash_string = TEST_MERCHANT_KEY + "|" + txnid + "|" + str(
        float(total_price)) + "|" + "info" + "|"
    hash_string += name + "|" + email + "|"
    hash_string += "||||||||||" + TEST_MERCHANT_SALT
    return hash_string


def get_transaction_id():
    hash_object = hashlib.sha256(str(randint(0, 9999)).encode("utf-8"))
    # take approprite length
    txnid = hash_object.hexdigest().lower()[0:32]
    return txnid


# no csrf token require to go to Success page.
# This page displays the success/confirmation message to user indicating the completion of transaction.
@csrf_exempt
def payment_success(request):
    data = {}
    print(str(data))
    return render(request, "payment/paymentsuccess.html", data)


# no csrf token require to go to Failure page. This page displays the message and reason of failure.
@csrf_exempt
def payment_failure(request):
    data = {}
    print(str(data))
    return render(request, "payment/paymentfail.html", data)
