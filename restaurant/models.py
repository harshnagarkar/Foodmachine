from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator
# from authentication.models import *
from authentication.models import User
# Create your models here.


class Cuisine(models.Model):
    def upload_image(self, filename):
        return 'post/{}/{}'.format(self.title, filename)
    Cuisine_Id = models.AutoField(primary_key=True)
    Cuisine_Sub = models.CharField(max_length=20, null=True)
    Cuisine_parent = models.CharField(max_length=20,null=True)
    Cuisine_Pic = models.ImageField(upload_to='media/', default='/media/defaultimage.png')


class Label(models.Model):
    # , null = false, blank = false)
    Label_Name = models.CharField(max_length=20)
    Label_Id = models.AutoField(primary_key=True)



class Restaurant(models.Model):

    def upload_image(self, filename):
        return 'post/{}/{}'.format(self.title.__str__(), filename)

    Res_Id = models.AutoField(primary_key=True)
    Res_Name = models.CharField(max_length=75)
    Res_Description = models.CharField(max_length=150, null=True)
    Res_Contact = PhoneNumberField(null=False, blank=False, unique=True)
    Res_Address = models.CharField(max_length=75)
    Cuisine_Type = models.ForeignKey(Cuisine, on_delete=models.SET_NULL, null=True,default=None)
    Res_Pic = models.ImageField(upload_to='media/', default='/media/defaultimage.png')


class Menu(models.Model):

    def upload_image(self, filename):
        return 'post/{}/{}'.format(self.title.__str__(), filename)
    
    Menu_Item_Id = models.AutoField(primary_key=True)
    Menu_Item = models.CharField(max_length=50)
    Menu_ItemPrice = models.DecimalField(max_digits=30, decimal_places=2)
    Menu_Item_Description = models.CharField(max_length=100)
    Menu_Res_Id = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=False, blank=False,default=None)
    Menu_Cuisine = models.ForeignKey(Cuisine, on_delete=models.SET_NULL, null= True, default=None)
    Menu_Label_Id = models.ForeignKey(Label, on_delete = models.SET_NULL,null=True)
    Menu_Pic = models.ImageField(upload_to='media/', default='/media/defaultimage.png')


class Review(models.Model):
    
    def upload_image(self, filename):
        return 'post/{}/{}'.format(self.title.__str__(), filename)
    
    Review_User = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    Review_Id = models.AutoField(primary_key=True)
    Res_Id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    Review_Des = models.CharField(max_length=75, blank=True)
    Review_Rating = models.IntegerField(  null=True, validators=[MaxValueValidator(5)])



