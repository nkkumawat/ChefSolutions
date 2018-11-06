from django.db import models

# Create your models here.


class Products(models.Model):
    id = models.IntegerField(primary_key=True)
    price = models.FloatField()
    b2b_price = models.FloatField()
    size = models.FloatField()
    energy = models.FloatField()  # Kcal
    protein = models.FloatField()  # gram
    carbohydrates = models.FloatField()  # gram
    sugar = models.FloatField()  # gram
    fat = models.FloatField()  # gram
    available_qty = models.IntegerField()  # how many packets are available
    #
    is_vegetarian = models.BooleanField(default=True)
    added_msg = models.BooleanField(default=True)
    name = models.CharField(max_length=100)
    shelf_life = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    storage = models.TextField(max_length=1000)
    uses = models.TextField(max_length=1000)
    benefits = models.TextField(max_length=1000)
    ingridients = models.TextField(max_length=1000)
    directions = models.TextField(max_length=1000)
    category = models.CharField(max_length=100)  # Filtering cateogry
    added_date = models.DateTimeField(auto_now=True)

    #     Nutritional value
    picture_1 = models.FileField(
        upload_to='static/products/images', blank=True)
    picture_2 = models.FileField(
        upload_to='static/products/images', blank=True)
    picture_3 = models.FileField(
        upload_to='static/products/images', blank=True)

    class Meta:
        db_table = "product"
