from django.db import models
from customer.models import Customers
# Create your models here.


class Recipes(models.Model):
    id = models.IntegerField(primary_key=True)
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    food_group = models.CharField(max_length=200) # dessert  ,baking

    use_of_products = models.CharField(max_length=1000) #saprated by $
    ingredients = models.TextField(max_length=2000)
#     cooking process
    cooking_process_name = models.CharField(max_length=100)
    cooking_process_method = models.TextField(max_length=2000)

    tags = models.CharField(max_length=100) # all are sparated with a #
    add_date = models.DateTimeField(auto_now=True)
    total_rating = models.IntegerField(default=0)
    total_users = models.IntegerField(default=0)

    is_apporved = models.BooleanField(default=False)
    video_url = models.TextField(default="")

    # picture_1 = models.FileField(upload_to='static/blog/recipe' , default='static/blog/recipe/default.png')
    # picture_2 = models.FileField(upload_to='static/blog/recipe' , default='static/blog/recipe/default.png')
    # picture_3 = models.FileField(upload_to='static/blog/recipe' , default='static/blog/recipe/default.png')

    class Meta:
        db_table = "recipe"