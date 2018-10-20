# Generated by Django 2.1.2 on 2018-10-13 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20181013_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipes',
            name='no_of_portions',
        ),
        migrations.RemoveField(
            model_name='recipes',
            name='use_of_goods',
        ),
        migrations.AddField(
            model_name='recipes',
            name='use_of_products',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipes',
            name='add_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]