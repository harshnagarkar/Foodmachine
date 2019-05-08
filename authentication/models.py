from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import post_save
from django.dispatch import receiver
from restaurant.models import Restaurant
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator

class UserProfile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   userType = models.CharField(max_length=1, choices=(('c',  ('Client')), ('r', ('Restaurant')),('d',  ('Delivery'))),default='c')
   userRestaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,null=True)
   Payment = models.IntegerField(
       validators=[MaxValueValidator(999999999999999)], null=True)
   Address = models.CharField(max_length=100,null=True)
   Phone = PhoneNumberField(null=True,blank=False)
   
def __str__(self):
    return self.user.username
		
		
