# Generated by Django 2.1.2 on 2018-11-05 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20181026_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='b2b_price',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]