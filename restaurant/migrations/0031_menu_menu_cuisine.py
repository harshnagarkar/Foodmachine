# Generated by Django 2.1.7 on 2019-03-31 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0030_remove_menu_menu_cuisine'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='Menu_Cuisine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.Cuisine'),
        ),
    ]
