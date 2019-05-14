
from django.contrib.auth.models import User
from django.apps import AppConfig
from authentication.models import UserProfile,User
import datetime
from django.utils import timezone 
from django.contrib.auth import authenticate, login


def userCreate(UserName, Password, Email, First_Name, Last_Name, UserType,UserRestaurant,Is_Staff='0'):
    try:
        user = User.objects.create_user(username=UserName, email=Email, password=Password, date_joined=datetime.datetime.now(),is_staff=Is_Staff,first_name=First_Name,last_name= Last_Name)
        userid = user.id
        userprofiles = UserProfile.objects.create(user_id = userid,Payment=None,Address=None,Phone = None,userType=UserType,userRestaurant=UserRestaurant)
        userprofiles.save()
        return 'success'
    except:
        return "Username exsist"


def updatePassword(Username,Password):
   u = User.objects.get(username=Username)
   u.set_password(Password)
   u.save()

class AuthenticationConfig(AppConfig):
    name = 'authentication'


def updateProf(username, firstName, lastName, email, phone, address, pay):

    u = User.objects.get(username__exact = username)
    u.first_name = firstName
    u.last_name = lastName
    u.email = email
    u.userprofile.Phone = phone
    u.userprofile.Address = address
    u.userprofile.Payment = pay

    u.save()
    u.userprofile.save()