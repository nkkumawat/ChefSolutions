# Generated by Django 2.1.2 on 2018-10-12 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20181012_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='customer_id',
            field=models.IntegerField(default=None, null=True),
        ),
    ]