# Generated by Django 2.1.2 on 2018-11-10 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20181110_0539'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='picture_1',
            field=models.FileField(default='static/blog/recipe/default.png', upload_to='static/blog/recipe'),
        ),
        migrations.AddField(
            model_name='recipes',
            name='picture_2',
            field=models.FileField(default='static/blog/recipe/default.png', upload_to='static/blog/recipe'),
        ),
        migrations.AddField(
            model_name='recipes',
            name='picture_3',
            field=models.FileField(default='static/blog/recipe/default.png', upload_to='static/blog/recipe'),
        ),
    ]
