from django.db import models
from customer.models import Customers
# Create your models here.


class Recipes(models.Model):
    id = models.IntegerField(primary_key=True)
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    food_group = models.CharField(max_length=200) # dessert  ,baking
    no_of_portions = models.IntegerField()
    use_of_goods = models.CharField(max_length=10) # low avg high
    ingredients = models.TextField(max_length=2000)
#     cooking process
    cooking_process_name = models.CharField(max_length=100)
    cooking_process_method = models.TextField(max_length=2000)

    tags = models.CharField(max_length=100) # all are sparated with a #
    add_date = models.DateField(auto_now=True)
    is_apporved = models.BooleanField(default=False)
    picture_1 = models.FileField(upload_to='static/blog/recipe' , default='static/blog/recipe/default.png')
    picture_2 = models.FileField(upload_to='static/blog/recipe' , default='static/blog/recipe/default.png')
    picture_3 = models.FileField(upload_to='static/blog/recipe' , default='static/blog/recipe/default.png')

    class Meta:
        db_table = "recipe"