# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Customers(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200 , unique=True)
    password = models.CharField(max_length=500)

    class Meta:
        db_table = "customer"

class Address(models.Model):
    id = models.IntegerField(primary_key=True)
    customer_id = models.IntegerField()
    address = models.CharField(max_length=500)

    class Meta:
        db_table = "address"




