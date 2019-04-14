from django import template
from django.shortcuts import render
from itertools import chain
# Create your views here.
from restaurant.models import Restaurant, Menu, Cuisine, Review
from authentication.models import UserProfile,User

register = template.Library()


@register.filter(name='getMenu')
def getMenu(resID):
    print(resID)
    context = Menu.objects.filter(Menu_Res_Id=resID)
    return context


@register.filter(name='getProfile')
def getProfile(usr):
    print(usr)
    context = User.objects.get(pk = (User.objects.get(username=usr).id))
    return context.userprofile.__dict__
