# Generated by Django 2.1.2 on 2018-10-13 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0012_customers_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='profile_pic',
            field=models.FileField(default='static/customer/default.png', upload_to='static/customers/profile'),
        ),
    ]