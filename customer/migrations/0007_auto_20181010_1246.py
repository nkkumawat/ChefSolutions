# Generated by Django 2.1.2 on 2018-10-10 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_auto_20181010_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='temp_id',
            field=models.CharField(default=None, max_length=500),
        ),
    ]
