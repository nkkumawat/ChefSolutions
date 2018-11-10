from django.db import models

# Create your models here.

class CouponCodes(models.Model):
    id = models.IntegerField(primary_key=True)
    coupon_code = models.CharField(max_length=16)
    is_applied = models.BooleanField(default=False)
    price_value = models.FloatField()
    class Meta:
        db_table = "coupon_code"
