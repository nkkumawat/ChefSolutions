# Generated by Django 2.1.2 on 2018-11-05 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20181013_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='cart_id',
            field=models.TextField(),
        ),
    ]
