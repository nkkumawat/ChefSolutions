from django.db import models
from customer.models import Customers
# Create your models here.


class Orders(models.Model):
    id = models.IntegerField(primary_key=True)
    cart_id = models.IntegerField()
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    total_price = models.FloatField()
    order_date = models.DateField(auto_now=True)
    payment_mode = models.CharField(max_length=100)
    is_payment_done = models.BooleanField(default=False)

    class Meta:
        db_table = "order"