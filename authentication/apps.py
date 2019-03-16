from django.contrib.auth.models import User
from django.apps import AppConfig
from authentication.models import UserProfile, User
from django.db import models
import datetime


def userCreate(UserName,Password,Email,First_Name,Last_Name,Is_Staff,Phone,Gender):
   user = User.objects.create_user(username=UserName, email=Email, password=Password, date_joined=datetime.datetime.now(),is_staff=Is_Staff,first_name=First_Name,last_name= Last_Name)
   # user.save()
   userp = User.objects.get(username=UserName).id
   userpc = UserProfile.objects.create(phone=Phone,gender=Gender,user_id = userp)
   userpc.save()
   return 'success'

def updatePassword(Username,Password):
   u = User.objects.get(username__exact=Username)
   u.set_password(Password)
   u.save()

class AuthenticationConfig(AppConfig):
    name = 'authentication'
