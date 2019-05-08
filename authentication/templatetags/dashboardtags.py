from django import template
from django.shortcuts import render
from itertools import chain
# Create your views here.
from authentication.models import UserProfile,User

register = template.Library()

#get profile content
@register.filter(name='getProfile')
def getProfile(usr):
    print(usr)
    context = User.objects.get(pk = (User.objects.get(username=usr).id))
    return context.userprofile.__dict__

