from django import template
from django.shortcuts import render
from itertools import chain
# Create your views here.
from restaurant.models import Restaurant, Menu, Cuisine, Review, Label
from authentication.models import UserProfile,User
import json
register = template.Library()


@register.filter(name='getMenu')
def getMenu(resID):
    print(resID)
    context = Menu.objects.filter(Menu_Res_Id=resID)
    return context

@register.filter(name = 'getRest')
def getRest(resID):
    context = Restaurant.objects.filter(Res_Id = resID)
    return context
    
@register.filter(name='getProfile')
def getProfile(usr):
    print(usr)
    context = User.objects.get(pk = (User.objects.get(username=usr).id))
    print(context.userprofile.__dict__)
    return context.userprofile.__dict__

@register.simple_tag
def getCuisine():
    cus = Cuisine.objects.values('Cuisine_parent')
    return cus

# @register.filter(name = 'getCuisine')
# def getCuisine(cusID):
#     print(cusID)
#     context = Cuisine.objects.filter(Cuisine_Id = cusID)
#     return context

@register.simple_tag
def getLabel():
    context = Label.objects.values('Label_Name')
    return context
