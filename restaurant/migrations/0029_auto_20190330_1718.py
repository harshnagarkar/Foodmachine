# Generated by Django 2.1.7 on 2019-03-30 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0028_auto_20190330_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='Menu_Res_Id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='restaurant.Restaurant'),
        ),
    ]
