# Generated by Django 2.1.7 on 2019-03-30 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0012_auto_20190330_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='Menu_Cusine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.Cuisine'),
        ),
    ]
