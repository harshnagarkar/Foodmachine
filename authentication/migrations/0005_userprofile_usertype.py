# Generated by Django 2.1.7 on 2019-03-27 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_remove_userprofile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='usertype',
            field=models.CharField(blank=True, choices=[('c', 'Client'), ('r', 'Restaurant'), ('d', 'Delivery')], default='c', max_length=1, null=True),
        ),
    ]
