# Generated by Django 2.1.7 on 2019-03-31 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0032_auto_20190331_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='Cuisine_Type',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.Cuisine'),
        ),
    ]
