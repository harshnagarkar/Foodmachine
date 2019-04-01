from django.db import models

# Create your models here.
class Orders(models.Model):
    Menu_Item = models.CharField(max_length=300)
    Order_Id = models.AutoField(primary_key=True)
    Restaurant_Id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    Preferences = models.CharField(max_length=300)
