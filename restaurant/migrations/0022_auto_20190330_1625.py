# Generated by Django 2.1.7 on 2019-03-30 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0021_auto_20190330_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='Cuisine_Type',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
