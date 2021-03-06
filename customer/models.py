# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Customers(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=500)
    mobile = models.CharField(max_length=10)
    temp_id = models.CharField(max_length=500, default='0')
    dob = models.DateField(default=None, null=True)
    is_active = models.BooleanField(default=False)
    is_b2b = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    profile_pic = models.FileField(
        upload_to='static/customer/profile', default="static/customer/profile/default.png")

    class Meta:
        db_table = "customer"


class Address(models.Model):
    id = models.IntegerField(primary_key=True)
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    street = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    state = models.CharField(max_length=500)
    country = models.CharField(max_length=500)
    pincode = models.IntegerField()

    class Meta:
        db_table = "address"



class RequestForB2B(models.Model):
    id = models.IntegerField(primary_key=True)
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    is_responsed = models.BooleanField(default=False)

    class Meta:
        db_table = "request_for_b2b"