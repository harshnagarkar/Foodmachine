# Generated by Django 2.1.7 on 2019-03-31 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0036_auto_20190331_0102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='Cuisine_Type',
        ),
    ]
