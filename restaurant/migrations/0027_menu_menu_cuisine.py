# Generated by Django 2.1.7 on 2019-03-30 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0026_auto_20190330_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='Menu_Cuisine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.Cuisine'),
        ),
    ]
