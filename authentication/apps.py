# from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.apps import AppConfig
from authentication.models import UserProfile,User
import datetime
from django.utils import timezone 
from django.contrib.auth import authenticate, login

def userCreate(UserName,Password,Email,First_Name,Last_Name,Answer,Question,Is_Staff='0'):
    try:
        user = User.objects.create_user(username=UserName, email=Email, password=Password, date_joined=datetime.datetime.now(),is_staff=Is_Staff,first_name=First_Name,last_name= Last_Name)
        userid = User.objects.get(username=UserName).id
        userprofiles = UserProfile.objects.create(question=Question,user_id = userid,answer = Answer)
        userprofiles.save()
        return 'success'
    except:
        return "Username exsist"


def loginuser(request):
    username = request.POST('username')
    password = request.POST('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        return user

    else:
        return 'Invalid Login details. Please try again!'



def updatePassword(Username,Password):
   u = User.objects.get(username__exact=Username)
   u.set_password(Password)
   u.save()

class AuthenticationConfig(AppConfig):
    name = 'authentication'
