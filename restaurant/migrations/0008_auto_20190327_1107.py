# Generated by Django 2.1.7 on 2019-03-27 16:07

from django.db import migrations, models
import restaurant.models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_restaurant_res_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='Res_Pic',
            field=models.ImageField(default='/media/defaultimage.png', upload_to=restaurant.models.Restaurant.upload_image),
        ),
    ]
