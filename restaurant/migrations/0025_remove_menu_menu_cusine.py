# Generated by Django 2.1.7 on 2019-03-30 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0024_auto_20190330_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='Menu_Cusine',
        ),
    ]