from django.db import models
from customer.models import Customers
from payment.models import Payment
# Create your models here.


class Orders(models.Model):
    id = models.IntegerField(primary_key=True)
    cart_id = models.TextField() # ids of cart saprated with $
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    total_price = models.FloatField()
    order_date = models.DateField(auto_now=True)
    payment_mode = models.CharField(max_length=100)
    is_payment_done = models.BooleanField(default=False)
    payment_id = models.ForeignKey(Payment , on_delete=models.CASCADE)
    class Meta:
        db_table = "order"