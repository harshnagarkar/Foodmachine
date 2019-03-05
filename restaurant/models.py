from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Restaurant(models.Model):
    Res_Id = models.AutoField(primary_key=True)
    Res_Name = models.CharField(max_length=75)
    Res_Description = models.CharField(max_length=150, null=True)
    Res_Contact = PhoneNumberField(null=False, blank=False, unique=True)
    Res_Address = models.CharField(max_length=75)
    Cuisine_Type = models.CharField(max_length=25)

    def __str__(self):              
        return self.Res_Name
    
class Menu(models.Model):
    Menu_Item_Id = models.AutoField(primary_key=True)
    Menu_Item = models.CharField(max_length=50)
    Menu_ItemPrice = models.IntegerField()
    Menu_Item_Description = models.CharField(max_length=100)
    Menu_Res_Id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
       return self.Menu_Item

class Review(models.Model):
    Review_Id = models.AutoField(primary_key=True)
    Res_Id = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    Review_Des = models.CharField(max_length = 75,blank=True)

    def __str__(self):
        return self.Review_Id

class Cuisine(models.Model):
    Cuisine_Id = models.AutoField(primary_key=True)
    Cusine_Sub = models.CharField(max_length=20)
    Cusine_parent = models.CharField(max_length=20,null=True)
    Menu_Item_Id = models.ForeignKey(Menu,on_delete=models.CASCADE)

    def __str__(self):
        return self.Cuisine_Id
