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
from .constants import PAID_FEE_AMOUNT, PAYMENT_URL_LIVE, PAYMENT_URL_TEST, PAID_FEE_PRODUCT_INFO
from .constants import SERVICE_PROVIDER


def payment(request):
    data = {}
    txnid = get_transaction_id()
    hash_ = generate_hash(request, txnid)
    hash_string = get_hash_string(request, txnid)
    # use constants file to store constant values.
    # use test URL for testing
    data["action"] = PAYMENT_URL_TEST
    data["amount"] = float(PAID_FEE_AMOUNT)
    data["productinfo"] = PAID_FEE_PRODUCT_INFO
    data["key"] = "UeAZKpo8"
    data["txnid"] = txnid
    data["hash"] = hash_
    data["hash_string"] = hash_string
    data["firstname"] = "nk"
    data["email"] = "nk@nk.com"
    data["phone"] = "9660729583"
    data["service_provider"] = SERVICE_PROVIDER
    data["furl"] = "http://localhost:8000/paymentfail"
    data["surl"] = "http://localhost:8000/paymentsuccess"

    return render(request, "payment/payment.html", data)


# generate the hash
def generate_hash(request, txnid):
    try:
        # get keys and SALT from dashboard once account is created.
        # hashSequence = "key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10"
        hash_string = get_hash_string(request, txnid)
        generated_hash = hashlib.sha512(
            hash_string.encode('utf-8')).hexdigest().lower()
        return generated_hash
    except Exception as e:
        # log the error here.
        logging.getLogger("error_logger").error(traceback.format_exc())
        return None


# create hash string using all the fields
def get_hash_string(request, txnid):
    hash_string = "UeAZKpo8" + "|" + txnid + "|" + str(
        float(PAID_FEE_AMOUNT)) + "|" + PAID_FEE_PRODUCT_INFO + "|"
    hash_string += "nk" + "|" + "nk@nk.com" + "|"
    hash_string += "||||||||||" + "OpMuojF2Xs"
    return hash_string


# generate a random transaction Id.
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
    return render(request, "payment/paymentsuccess.html", data)


# no csrf token require to go to Failure page. This page displays the message and reason of failure.
@csrf_exempt
def payment_failure(request):
    data = {}
    return render(request, "payment/paymentfail.html", data)
