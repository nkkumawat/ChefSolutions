# Generated by Django 2.1.2 on 2018-10-22 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0015_auto_20181022_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='address',
            name='pincode',
            field=models.IntegerField(),
        ),
    ]
