# Generated by Django 2.1.7 on 2019-03-27 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_label'),
        ('authentication', '0005_userprofile_usertype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='usertype',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='userRestaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.Restaurant'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='userType',
            field=models.CharField(choices=[('c', 'Client'), ('r', 'Restaurant'), ('d', 'Delivery')], default='c', max_length=1),
        ),
    ]
