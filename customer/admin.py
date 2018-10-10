# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Customers , Address
# Register your models here.

admin.site.register(Customers)
admin.site.register(Address)
