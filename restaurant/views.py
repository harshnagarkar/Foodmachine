from django.shortcuts import render
from itertools import chain
# Create your views here.
from .models import Restaurant,Menu,Cuisine,Review


def restaurantPage(request, restaurantName):
    resDetail = Restaurant.objects.get(Res_Name=restaurantName).__dict__
    return render(request, 'restaurant/restaurant.html', resDetail)

def processMenu(request):

    print (request.POST)
    return render(request,'create-menu.html')

def createMenuItems(request):
    itemCreate = Menu.objects.create(Menu_Item ='test', Menu_ItemPrice = 0, Menu_Description = 'test' )
    itemCreate.save()
    #priceCreate = Menu.objects.create(Menu_ItemPrice = 0 )
    #descriptCreate = Menu.objects.create(Menu_Description = 'test')
    return render(request, 'create-menu.html')
def createLabel(request):
    labelCreate = Label.objects.create(Label_Name = '')


