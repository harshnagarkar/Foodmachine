from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.

class UserProfile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   phone = models.CharField(max_length=256, blank=True, null=True)
   gender = models.CharField(
        max_length=1, choices=(('m',  ('Male')), ('f', ('Female'))),blank=True, null=True)