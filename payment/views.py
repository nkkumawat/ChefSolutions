from django.shortcuts import render, reverse

# Create your views here.

from django.shortcuts import render, redirect
import hashlib
from random import randint
from django.views.decorators.csrf import csrf_exempt
from .constants import PAYMENT_URL_TEST, PAID_FEE_PRODUCT_INFO
from .constants import SERVICE_PROVIDER, TEST_MERCHANT_KEY, TEST_MERCHANT_SALT
from cart.models import Cart
from customer.models import Customers
from .models import Payment
from order.models import Orders
from django.core.mail import EmailMessage
import utils

def payment(request):
    if 'customer_id' in request.session:
        cart_details = Cart.objects.filter(customer_id=request.session['customer_id'], is_purchased=False)
        if cart_details.__len__() == 0:
            return render(request, "payment/noitemsincart.html")
        else:
            total_price = 0.0
            for cart in cart_details:
                total_price += cart.quantity * cart.product_id.price
            customer = Customers.objects.filter(id=request.session['customer_id'])[0]
            data = {}
            txnid = get_transaction_id()
            hash = generate_hash(request, txnid, total_price, customer.name.split(" ")[0], customer.email, customer.id)
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
            data["furl"] = request.build_absolute_uri(reverse("payment:payment_success"))
            data["surl"] = request.build_absolute_uri(reverse("payment:payment_success"))
            data["udf1"] = request.session["customer_id"]
            return render(request, "payment/payment.html", data)
    else:
        return redirect('error:error')


def generate_hash(request, txnid, total_price, name, email, customer_id):
    try:
        hash_string = get_hash_string(request, txnid, total_price, name, email, customer_id)
        generated_hash = hashlib.sha512(
            hash_string.encode('utf-8')).hexdigest().lower()
        return generated_hash
    except Exception as e:
        print(e)
        return None


def get_hash_string(request, txnid, total_price, name, email, customer_id):
    hash_string = TEST_MERCHANT_KEY + "|" + txnid + "|" + str(
        float(total_price)) + "|" + "info" + "|"
    hash_string += name + "|" + email + "|" + str(customer_id) + "|"
    hash_string += "|||||||||" + TEST_MERCHANT_SALT
    return hash_string


def get_transaction_id():
    hash_object = hashlib.sha256(str(randint(0, 9999)).encode("utf-8"))
    txnid = hash_object.hexdigest().lower()[0:32]
    return txnid


@csrf_exempt
def payment_success(request):
    data = {}
    if request.method == "POST":
        payment = Payment()
        payment.mode = request.POST['mode']
        payment.hash = request.POST['hash']
        payment.status = request.POST['status']
        payment.txnid = request.POST['txnid']
        payment.amount = request.POST['amount']
        payment.bank_ref_num = request.POST['bank_ref_num']
        payment.mihpayid = request.POST['mihpayid']
        payment.pg_type = request.POST['PG_TYPE']
        payment.productinfo = request.POST['productinfo']
        payment.error = request.POST['error']
        payment.card_category = request.POST['cardCategory']
        payment.discount = request.POST['discount']
        payment.net_amount_debit = request.POST['net_amount_debit']
        payment.payment_source = request.POST['payment_source']
        payment.bank_code = request.POST['bankcode']
        payment.error_message = request.POST['error_Message']
        payment.card_num = request.POST['cardnum']
        payment.name_on_card = request.POST['name_on_card']
        payment.cardhash = request.POST['cardhash']
        payment.issuing_bank = request.POST['issuing_bank']
        payment.card_type = request.POST['card_type']
        payment.customer_id = Customers.objects.filter(id=request.POST['udf1'])[0]
        payment.save()

        orders = Orders()
        cart_details = Cart.objects.filter(customer_id=request.POST['udf1'], is_purchased=False)
        cart_ids = ""
        for cart in cart_details:
            cart_ids += str(cart.id) + "$"
        orders.cart_id = cart_ids
        orders.customer_id = Customers.objects.filter(id=request.POST['udf1'])[0]
        orders.total_price = request.POST['amount']
        orders.payment_mode = request.POST['mode']
        orders.is_payment_done = True
        orders.payment_id = Payment.objects.filter(txnid=request.POST['txnid'],
                                                   customer_id=Customers.objects.filter(id=request.POST['udf1'])[0])[0]
        orders.save()
        cart_details.update(is_purchased=True)
        customer = Customers.objects.filter(id=request.POST['udf1'])[0]
        body = "New Order Received from user: " + customer.name + "\n "
        body += "Email : " + str(customer.email) + "\n"
        body += "Mobile: " + str(customer.mobile)

        email = EmailMessage('Chef Solutions', body, to=utils.our_emails)
        email.send()

        body = ""
        body += "Thanks for Choosing ChefSolutions"
        body += "orderId: " +str(Orders.objects.filter(cart_id=cart_ids , customer_id=customer)[0].id)
        print(body)

        email = EmailMessage('Chef Solutions', body, to=[customer.email])
        email.send()

        return render(request, "payment/paymentsuccess.html", data)
    return redirect('error:error')


@csrf_exempt
def payment_failure(request):
    data = {}
    print(str(data))
    if request.method == "POST":
        payment = Payment()
        payment.mode = request.POST['mode']
        payment.hash = request.POST['hash']
        payment.status = request.POST['status']
        payment.txnid = request.POST['txnid']
        payment.amount = request.POST['amount']
        payment.bank_ref_num = request.POST['bank_ref_num']
        payment.mihpayid = request.POST['mihpayid']
        payment.pg_type = request.POST['PG_TYPE']
        payment.productinfo = request.POST['productinfo']
        payment.error = request.POST['error']
        payment.card_category = request.POST['cardCategory']
        payment.discount = request.POST['discount']
        payment.net_amount_debit = request.POST['net_amount_debit']
        payment.payment_source = request.POST['payment_source']
        payment.bank_code = request.POST['bankcode']
        payment.error_message = request.POST['error_Message']
        payment.card_num = request.POST['cardnum']
        payment.name_on_card = request.POST['name_on_card']
        payment.cardhash = request.POST['cardhash']
        payment.issuing_bank = request.POST['issuing_bank']
        payment.card_type = request.POST['card_type']
        payment.customer_id = Customers.objects.filter(id=request.POST['udf1'])[0]
        payment.save()
        return render(request, "payment/paymentfail.html", data)

    return redirect('error:error')
