from django import template
from django.shortcuts import render
from itertools import chain

from authentication.models import UserProfile, User

register = template.Library()


@register.filter(name='getProfile')
def getProfile(usr):
    print(usr)
    context = User.objects.get(pk=(User.objects.get(username=usr).id))
    return context.userprofile.__dict__
