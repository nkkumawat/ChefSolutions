# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from django.utils.crypto import get_random_string
from django.core.mail import EmailMessage

from .forms import loginForm, signUpForm
from .models import Customers, Address
from cart.models import Cart

data = {
    "title": "Chef Solutions",
    "message": ""
}


def login(request):
    data['message'] = ""
    if 'customer_id' not in request.session:
        if request.method == 'POST':
            loginform = loginForm(request.POST)
            if loginform.is_valid():
                email = loginform.cleaned_data['email']
                password = loginform.cleaned_data['password']
                customer = Customers.objects.filter(email=email)
                if customer:
                    if check_password(password, customer[0].password):
                        if customer[0].is_active:
                            request.session['customer_id'] = customer[0].id
                            if 'temp_customer_id' in request.session:
                                cart = Cart.objects.filter(
                                    temp_customer_id=request.session['temp_customer_id'])
                                cart.update(
                                    temp_customer_id='0', customer_id=request.session['customer_id'])
                                del request.session['temp_customer_id']
                            return redirect('customer:profile')
                        else:
                            data['message'] = "Your account is not activated yet"
                            return render(request, "customer/login.html", data)
                    else:
                        data['message'] = "Password Incorrect"
                        return render(request, "customer/login.html", data)
                else:
                    data['message'] = "User not exists"
                    return render(request, "customer/login.html", data)
            else:
                data['message'] = "Invalid Form"
                return render(request, "customer/login.html", data)
        else:
            if 'customer_id' in request.session:
                return redirect('customer:profile')
            else:
                return render(request, "customer/login.html", data)
    else:
        return redirect("customer:profile")


def signup(request):
    data['message'] = ""
    if 'customer_id' not in request.session:

        if request.method == 'POST':
            signupform = signUpForm(request.POST)
            if signupform.is_valid():
                email = signupform.cleaned_data['email']
                password = signupform.cleaned_data['password']
                name = signupform.cleaned_data['name']
                mobile = signupform.cleaned_data['mobile']
                if Customers.objects.filter(email=email):
                    data['message'] = "Email alreay Exists"
                    return render(request, "customer/signup.html", data)
                else:
                    customer = Customers()
                    customer.name = name
                    customer.email = email
                    customer.password = make_password(password)
                    customer.mobile = mobile
                    customer.temp_id = get_random_string(length=200)
                    customer.save()

                    body = "Please click on below link for Account verification\n "
                    body += "http://localhost:8000/customer/verify?id=" + customer.temp_id
                    email = EmailMessage('Chef Solutions', body, to=[email])
                    email.send()
                    data['message'] = "check your email for account varification"
                    return render(request, "customer/signup.html", data)
            else:
                return redirect('error:error')
        else:
            return render(request, "customer/signup.html", data)
    else:
        return redirect("error:error")


def profile(request):
    data['message'] = ""
    if 'customer_id' in request.session:
        customer = Customers.objects.filter(id=request.session['customer_id'])
        data["name"] = customer[0].name
        data["email"] = customer[0].email
        data["image"] = customer[0].profile_pic
        address = Address.objects.filter(
            customer_id=Customers.objects.filter(id=request.session['customer_id'])[0])
        data['address'] = address
        return render(request, "customer/profile.html", data)
    else:
        return redirect('customer:login')


def logout(request):
    data['message'] = ""
    if 'customer_id' in request.session:
        del request.session['customer_id']
        return redirect('index')
    else:
        return redirect('customer:login')


def forgotPassword(request):
    data['message'] = ""
    if request.method == "POST":
        email = request.POST["email"]
        customer = Customers.objects.filter(email=email)
        if customer:
            temp_id = get_random_string(length=200)
            customer.update(temp_id=temp_id)
            body = "Please click on below link for password change\n "
            body += "http://localhost:8000/customer/forgotpassword?id="+temp_id
            email = EmailMessage('Chef Solutions', body, to=[email])
            email.send()
            data['message'] = "Email sent to Your email"
            return render(request, "customer/forgotpassword.html", data)
        else:
            data['message'] = "No Such Customer"
            return render(request, "customer/forgotpassword.html", data)
    else:
        if 'id' in request.GET:
            id = request.GET['id']
            if id != '0':
                customer = Customers.objects.filter(temp_id=id)
                if customer:
                    data['temp_id'] = id
                    return render(request, "customer/changepassword.html", data)
                else:
                    data['message'] = "wrong request"
                    return render(request, "customer/forgotpassword.html", data)
            else:
                data['message'] = "wrong request"
                return render(request, "customer/forgotpassword.html", data)
        else:
            return render(request, "customer/forgotpassword.html", data)


def changePassword(request):  # for forgot password
    data['message'] = ""
    if request.method == "POST":
        temp_id = request.POST['temp_id']
        password = request.POST['password']
        if temp_id != '0':
            customer = Customers.objects.filter(temp_id=temp_id)
            if customer:
                customer.update(password=make_password(password))
                customer.update(temp_id='0')
                return redirect('customer:login')
            else:
                return redirect('error:error')
        else:
            return redirect('error:error')
    else:
        return redirect('error:error')


def accoutVarification(request):
    data['message'] = ""
    if 'id' in request.GET:
        id = request.GET['id']
        if id != '0':
            customer = Customers.objects.filter(temp_id=id)
            if customer:
                customer.update(is_active=True, temp_id='0')
                return redirect('customer:login')
            else:
                return redirect('error:error')
        else:
            return redirect('error:error')
    else:
        return redirect('error:error')


def updatePassword(request):
    data['message'] = ""
    if 'customer_id' in request.session:
        if request.method == "POST":
            oldPassword = request.POST['oldPassword']
            newPassword = request.POST['newPassword']
            customer = Customers.objects.filter(
                id=request.session['customer_id'])
            if check_password(oldPassword, customer[0].password):
                customer.update(password=make_password(newPassword))
                data['message'] = "password changed successfully"
                return render(request, "customer/updatepassword.html", data)
            else:
                data['message'] = "Old password is not correct"
                return render(request, "customer/updatepassword.html", data)
        else:
            return render(request, "customer/updatepassword.html", data)
    else:
        return redirect("error:error")


def updateProfile(request):
    data['message'] = ""
    if 'customer_id' in request.session:
        if request.method == "POST":
            add = request.POST['address']
            dob = request.POST['dob']
            address = Address()
            address.customer_id = Customers.objects.filter(
                id=request.session['customer_id'])[0]
            address.address = add
            address.save()

            customer = Customers.objects.filter(
                id=request.session['customer_id'])
            customer.update(dob=dob)
            data['message'] = "Updated Successfully"
            return render(request, "customer/updateprofile.html", data)
        else:
            return render(request, "customer/updateprofile.html", data)
    else:
        return redirect("error:error")
