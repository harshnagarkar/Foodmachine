# Generated by Django 2.1.7 on 2019-03-31 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0037_remove_restaurant_cuisine_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='Menu_Res_Id',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
    ]