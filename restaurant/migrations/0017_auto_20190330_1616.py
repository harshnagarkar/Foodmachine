# Generated by Django 2.1.7 on 2019-03-30 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0016_auto_20190330_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='Menu_Cusine',
            field=models.ForeignKey(default='null', null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.Cuisine'),
        ),
    ]
