from django.db import models
from restaurant.models import *
from django.core.validators import MaxValueValidator
# Create your models here.
from datetime import datetime, timedelta


class Orders(models.Model):
    Menu_Item = models.CharField(max_length=300)
    Order_Id = models.AutoField(primary_key=True)
    Restaurant_Id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    Preferences = models.CharField(max_length=300)
    Status = models.CharField(max_length=1, choices=(('s',  ('submitted')), ('r', ('Restaurant')), ('d',  ('Delivery')), ('e',  ('Declined'))), default='s')
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='user')
    Price = models.FloatField(null=True, blank=True, default=None)
    Payment = models.IntegerField(
        null=True, validators=[MaxValueValidator(999999999999999)])
    Deliverer = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='Deliverer')
    orderDate = models.DateTimeField(default=datetime.now())
