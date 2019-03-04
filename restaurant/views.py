from django.shortcuts import render
from itertools import chain
# Create your views here.
from .models import Restaurant,Menu,Cuisine,Review


def restaurantPage(request, restaurantName):
    resDetail = Restaurant.objects.get(Res_Name=restaurantName).__dict__
    return render(request, 'restaurant/restaurant.html', resDetail)


def getMenu(resID):
    context = Menu.objects.filter(Menu_Res_Id=1).values()
    return context
