# Generated by Django 2.1.2 on 2018-11-03 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20181026_1131'),
        ('cart', '0007_remove_cart_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.Products'),
            preserve_default=False,
        ),
    ]
