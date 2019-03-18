# from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.apps import AppConfig
from authentication.models import UserProfile,User
import datetime
from django.utils import timezone 


def userCreate(UserName,Password,Email,First_Name,Last_Name,Is_Staff='0',Phone,Gender='m'):
    try:
        user = User.objects.create_user(username=UserName, email=Email, password=Password, date_joined=datetime.datetime.now(),is_staff=Is_Staff,first_name=First_Name,last_name= Last_Name)
        userid = User.objects.get(username=UserName).id
        userprofiles = UserProfile.objects.create(phone=Phone,gender=Gender,user_id = userid)
        userprofiles.save()
        return 'success'
    except:
        return "Username exsist"

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
