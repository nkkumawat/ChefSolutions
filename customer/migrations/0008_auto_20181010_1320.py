# Generated by Django 2.1.2 on 2018-10-10 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_auto_20181010_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='temp_id',
            field=models.CharField(default='0', max_length=500),
        ),
    ]