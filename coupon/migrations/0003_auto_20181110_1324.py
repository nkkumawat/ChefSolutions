# Generated by Django 2.1.2 on 2018-11-10 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0002_auto_20181110_1321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='couponcodes',
            old_name='discount_percentage',
            new_name='price_value',
        ),
    ]
