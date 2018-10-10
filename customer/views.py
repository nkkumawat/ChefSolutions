# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password

from .forms import loginForm, signUpForm
from .models import Customers


def login(request):
    data = {
        "title": "Chef Solutions",
        "error": ""
    }
    if request.method == 'POST':
        loginform = loginForm(request.POST)
        if loginform.is_valid():
            email = loginform.cleaned_data['email']
            password = loginform.cleaned_data['password']
            customer = Customers.objects.get(email=email)
            if customer:
                if check_password(password, customer.password):
                    request.session['customer_id'] = customer.id
                    return HttpResponseRedirect('dashboard')
                else:
                    data['error'] = "Password Incorrect"
                    return render(request, "customer/login.html", data)
            else:
                data['error'] = "User not exists"
                return render(request, "customer/login.html", data)
        else:
            data.error = "Invalid Form"
            return render(request, "customer/login.html", data)
    else:
        if 'customer_id' in request.session:
            return HttpResponseRedirect('dashboard')
        else:
            return render(request, "customer/login.html", data)


def signup(request):
    data = {
        "title": "Chef Solutions",
        "error": ""
    }
    if request.method == 'POST':
        signupform = signUpForm(request.POST)
        if signupform.is_valid():
            email = signupform.cleaned_data['email']
            password = signupform.cleaned_data['password']
            name = signupform.cleaned_data['name']
            if Customers.objects.get(email=email):
                data['error'] = "Email alreay Exists"
                return render(request, "customer/signup.html", data)
            else:
                customer = Customers()
                customer.name = name
                customer.email = email
                customer.password = make_password(password)
                customer.save()
                request.session['customer_id'] = Customers.objects.get(email=customer.email).id
                return HttpResponseRedirect('dashboard')
        else:
            return render(request, "error.html")
    else:
        return render(request, "customer/signup.html", data)


def dashboard(request):
    if 'customer_id' in request.session:
        customer = Customers.objects.get(id=request.session['customer_id'])
        data = {
            "title": "Chef Solutions",
            "name": customer.name,
            "email": customer.email
        }
        return render(request, "customer/dashboard.html", data)
    else:
        return HttpResponseRedirect('login')


def logout(request):
    if 'customer_id' in request.session:
        del request.session['customer_id']
        return HttpResponseRedirect('login')
    else:
        return HttpResponseRedirect('login')
