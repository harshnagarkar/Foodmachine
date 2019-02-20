from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Restaurant(models.Model):
    Res_Id = models.AutoField(primary_key=True)
    Res_Name = models.CharField(max_length=75)
    Res_Description = models.CharField(max_length=150)
    Res_Contact = PhoneNumberField(null=False, blank=False, unique=True)
    Res_Location = models.CharField(max_length=25)
    Res_Address = models.CharField(max_length=75)
    Cuisine_Type = models.CharField(max_length=25)
    
class Menu(models.Model):
    Menu_Item_Id = models.AutoField(primary_key=True)
    Menu_Item = models.CharField(max_length=50)
    Menu_ItemPrice = models.IntegerField()
    Menu_Item_Description = models.CharField(max_length=100)
    Menu_Res_Id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)