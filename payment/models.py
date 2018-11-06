from __future__ import unicode_literals

from django.db import models
from customer.models import Customers
# Create your models here.


class Payment(models.Model):
    id = models.IntegerField(primary_key=True)
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE) #udf1
    mode = models.CharField(max_length=2)
    status = models.CharField(max_length=10)
    txnid = models.CharField(max_length=40)
    amount = models.FloatField()
    productinfo = models.TextField()
    hash = models.TextField()
    error = models.TextField()
    pg_type = models.CharField(max_length=11)
    bank_ref_num = models.CharField(max_length=21)
    mihpayid = models.TextField()

    # payumoneyId = models.CharField(max_length=10)
    # additional_charges = models.TextField()

    card_category = models.TextField()
    discount = models.FloatField()
    net_amount_debit = models.FloatField()
    payment_source = models.TextField()
    bank_code = models.TextField()
    error_message = models.TextField()
    card_num = models.CharField(max_length=20)
    name_on_card = models.CharField(max_length=30)
    cardhash = models.TextField()
    issuing_bank = models.TextField()
    card_type = models.CharField(max_length=20)
    class Meta:
        db_table = "payments"


