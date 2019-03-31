from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import post_save
from django.dispatch import receiver
from restaurant.models import Restaurant
# Create your models here.

class UserProfile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   # phone = models.CharField(max_length=256, blank=True, null=True)
   question= models.CharField(max_length=60, null=True)
   answer = models.CharField(max_length = 50, null=True)
   userType = models.CharField(max_length=1, choices=(('c',  ('Client')), ('r', ('Restaurant')),('d',  ('Delivery'))),default='c')
   userRestaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,null=True)
   
		
		
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

# createUser(UserName='test',Password='test',Email='test@gmail.com',First_Name='test1',Last_Name='test2',Question='what is name',secAnswer
   # ...: ='mom',Is_Staff='0')
