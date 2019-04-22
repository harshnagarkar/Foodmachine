from django.db import models
from restaurant.models import *
# Create your models here.
class Orders(models.Model):
    Menu_Item = models.CharField(max_length=300)
    Order_Id = models.AutoField(primary_key=True)
    Restaurant_Id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    Preferences = models.CharField(max_length=300)
    Status  = models.CharField(max_length=1, choices=(('s',  ('submitted')), ('r', ('Restaurant')),('d',  ('Delivery'))),default='s')
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    Price = models.FloatField(null=True, blank=True, default=None)

