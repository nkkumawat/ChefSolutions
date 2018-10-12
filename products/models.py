from django.db import models

# Create your models here.

class Products(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    size = models.FloatField()
    description = models.TextField(max_length=1000)
    storage = models.TextField(max_length=1000)
    shelf_life = models.CharField(max_length=100)
    uses = models.TextField(max_length=1000)
    benefits = models.TextField(max_length=1000)
#     Nutritional value
    energy = models.FloatField() # Kcal
    protein = models.FloatField() #gram
    carbohydrates = models.FloatField() # gram
    suger = models.FloatField() #gram
    fat = models.FloatField() #gram

    ingridients = models.TextField(max_length=1000)
    directions = models.TextField(max_length=1000)
    picture_1 = models.FileField(upload_to='static/products/images', blank=True)
    picture_2 = models.FileField(upload_to='static/products/images', blank=True)
    picture_3 = models.FileField(upload_to='static/products/images', blank=True)


    available_qty = models.IntegerField() # how many packets are available

    added_date = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = "product"