from django.db import models

# Create your models here.

class Cart(models.Model):
    id = models.IntegerField(primary_key=True)
    customer_id = models.IntegerField()
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now=True)
    is_purchased = models.BooleanField(default=False)

    class Meta:
        db_table = "cart"
