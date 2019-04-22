from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import post_save
from django.dispatch import receiver
from restaurant.models import Restaurant
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class UserProfile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   # phone = models.CharField(max_length=256, blank=True, null=True)
   userType = models.CharField(max_length=1, choices=(('c',  ('Client')), ('r', ('Restaurant')),('d',  ('Delivery'))),default='c')
   userRestaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,null=True)
   Payment = models.IntegerField(max_length=15,null=True)
   Address = models.CharField(max_length=100,null=True)
   Phone = PhoneNumberField(null=True,blank=False)
   
def __str__(self):
    return self.user.username
		
		
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

# createUser(UserName='test',Password='test',Email='test@gmail.com',First_Name='test1',Last_Name='test2',Question='what is name',secAnswer
   # ...: ='mom',Is_Staff='0')
