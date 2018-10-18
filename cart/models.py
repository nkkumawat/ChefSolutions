from django.db import models
from customer.models import Customers
# Create your models here.
from products.models import Products
from django.db.models import Sum


class Cart(models.Model):
    id = models.IntegerField(primary_key=True)
    customer_id = models.IntegerField(default=None, null=True)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now=True)
    temp_customer_id = models.CharField(max_length=300, default="0")
    is_purchased = models.BooleanField(default=False)

    class Meta:
        db_table = "cart"
