from django.shortcuts import render
from itertools import chain
# Create your views here.
from .models import Restaurant,Menu,Cuisine,Review


def restaurantPage(request, restaurantName):
    resDetail = Restaurant.objects.get(Res_Name=restaurantName)
    menuItems = Menu.objects.get(Menu_Item_Id=resDetail.Res_Id)
    context = {**resDetail.__dict__,**menuItems.__dict__}
    return render(request, 'restaurant/restaurant.html', context)
