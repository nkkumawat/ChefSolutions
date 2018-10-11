# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from django.utils.crypto import get_random_string
from django.core.mail import EmailMessage

from .forms import loginForm, signUpForm
from .models import Customers, Address

data = {
        "title": "Chef Solutions",
        "message": ""
    }
def login(request):
    data['message'] = ""
    if request.method == 'POST':
        loginform = loginForm(request.POST)
        if loginform.is_valid():
            email = loginform.cleaned_data['email']
            password = loginform.cleaned_data['password']
            customer = Customers.objects.filter(email=email)
            if customer:
                if check_password(password, customer[0].password):
                    if  customer[0].is_active:
                        request.session['customer_id'] = customer[0].id
                        return HttpResponseRedirect('dashboard')
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
            return HttpResponseRedirect('dashboard')
        else:
            return render(request, "customer/login.html", data)


def signup(request):
    data['message'] = ""
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

                body = "Please click on below link for Account varification\n "
                body += "http://localhost:8000/customer/varify?id=" + customer.temp_id
                email = EmailMessage('Chef Solutions', body, to=[email])
                email.send()
                data['message'] = "check your email for account varification"
                return render(request, "customer/signup.html", data)
        else:
            return render(request, "error.html")
    else:
        return render(request, "customer/signup.html", data)


def dashboard(request):
    data['message'] = ""
    if 'customer_id' in request.session:
        customer = Customers.objects.filter(id=request.session['customer_id'])
        data["name"] = customer[0].name
        data["email"] = customer[0].email
        address = Address.objects.filter(customer_id=request.session['customer_id'])
        data['address'] = address
        return render(request, "customer/dashboard.html", data)
    else:
        return HttpResponseRedirect('login')


def logout(request):
    data['message'] = ""
    if 'customer_id' in request.session:
        del request.session['customer_id']
        return HttpResponseRedirect('login')
    else:
        return HttpResponseRedirect('login')

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
            data['message'] = "Email sent to this email"
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
                    return render(request, "customer/changepassword.html", data)
                else:
                    data['message'] = "wrong request"
                    return render(request, "customer/forgotpassword.html", data)
            else:
                data['message'] = "wrong request"
                return render(request, "customer/forgotpassword.html", data)
        else:
            return render(request, "customer/forgotpassword.html", data)


def changePassword(request): # for forgot password
    data['message'] = ""
    if request.method == "POST":
        temp_id = request.POST['temp_id']
        password = request.POST['password']
        if temp_id != '0':
            customer = Customers.objects.filter(temp_id=temp_id)
            if customer:
                customer.update(password=make_password(password))
                customer.update(temp_id='0')
                return HttpResponseRedirect('login')
            else:
               return HttpResponseRedirect('/error')
        else:
            return HttpResponseRedirect('/error')
    else:
       return HttpResponseRedirect('/error')


def accoutVarification(request):
    data['message'] = ""
    if 'id' in request.GET:
        id = request.GET['id']
        if id != '0':
            customer = Customers.objects.filter(temp_id=id)
            if customer:
                customer.update(is_active=True , temp_id='0')
                return HttpResponseRedirect('login')
            else:
                return HttpResponseRedirect('/error')
        else:
            return HttpResponseRedirect('/error')
    else:
        return HttpResponseRedirect('/error')

def updatePassword(request):
    data['message'] = ""
    if 'customer_id' in request.session:
        if request.method == "POST":
            oldPassword = request.POST['oldPassword']
            newPassword = request.POST['newPassword']
            customer = Customers.objects.filter(id=request.session['customer_id'])
            if check_password(oldPassword , customer[0].password):
                customer.update(password=make_password(newPassword))
                data['message'] = "password changed succss"
                return render(request, "customer/updatepassword.html", data)
            else:
                data['message'] = "Old password is not correct"
                return render(request, "customer/updatepassword.html", data)
        else:
            return render(request, "customer/updatepassword.html", data)
    else:
        return HttpResponseRedirect("/error")

def updateProfile(request):
    data['message'] = ""
    if 'customer_id' in request.session:
        if request.method == "POST":
            add = request.POST['address']
            address = Address()
            address.customer_id = request.session['customer_id']
            address.address = add
            address.save()
            data['message'] = "Updated Success"
            return render(request, "customer/updateprofile.html", data)
        else:
            return render(request, "customer/updateprofile.html", data)
    else:
        return HttpResponseRedirect("/error")
