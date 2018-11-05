# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Customers , Address
# Register your models here.

class CustomerDetails(admin.ModelAdmin):
    list_display = ('id' , 'name', 'email', 'mobile', 'dob', 'is_active' , 'profile_pic')

class AddressDetails(admin.ModelAdmin):
    list_display = ('id' , 'customer_id', 'street', 'city', 'state', 'country' , 'pincode')


admin.site.register(Customers)
admin.site.register(Address )
