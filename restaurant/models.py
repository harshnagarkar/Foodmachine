from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator

# Create your models here.
class Restaurant(models.Model):
    
    def upload_image(self, filename):
        return 'post/{}/{}'.format(self.title, filename)

    Res_Id = models.AutoField(primary_key=True)
    Res_Name = models.CharField(max_length=75)
    Res_Description = models.CharField(max_length=150, null=True)
    Res_Contact = PhoneNumberField(null=False, blank=False, unique=True)
    Res_Address = models.CharField(max_length=75)
    Cuisine_Type = models.CharField(max_length=25)
    Res_Pic = models.ImageField(upload_to=upload_image, default='/media/defaultimage.png')


    
class Menu(models.Model):
    Menu_Item_Id = models.AutoField(primary_key=True)
    Menu_Item = models.CharField(max_length=50)
    Menu_ItemPrice = models.DecimalField(max_digits = 30, decimal_places = 2)
    Menu_Item_Description = models.CharField(max_length=100)
    Menu_Res_Id = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null = 'false', blank = 'false')
    #Menu_Label_Id = models.ForeignKey(Label, on_delete = models.CASCADE)

class Label(models.Model):
    Label_Name = models.CharField(max_length=20)#, null = false, blank = false)
    Label_Id = models.AutoField(primary_key = True)
    Label_Menu_Id = models.ForeignKey(Menu, on_delete = models.CASCADE)
    
class Review(models.Model):
    Review_Id = models.AutoField(primary_key=True)
    Res_Id = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    Review_Des = models.CharField(max_length = 75,blank=True)
    Review_Rating = models.IntegerField(null=True, validators=[MaxValueValidator(5)])

class Cuisine(models.Model):
    Cuisine_Id = models.AutoField(primary_key=True)
    Cusine_Sub = models.CharField(max_length=20)
    Cusine_parent = models.CharField(max_length=20,null=True)
    Menu_Item_Id = models.ForeignKey(Menu,on_delete=models.CASCADE)
    Menu_Item_Id = models.ForeignKey(Menu,on_delete=models.CASCADE)

    def __str__(self):
        return self.Cuisine_Id
