from django.shortcuts import render
from itertools import chain
# Create your views here.
from .models import Restaurant,Cuisine,Review, Label
from restaurant.forms import *

def createRestaurant(request):
     if request.method == 'POST':
        #Rest = request.POST['Rest']
        if request.method == "POST":
            form = RestaurantCreation(request.POST, request.FILES)
            print(form.errors)
            print(form.is_valid())
            if form.is_valid():
                resname = form.cleaned_data.get('resname')
                resdescription = form.cleaned_data.get('resdescription')
                rescontact = form.cleaned_data.get('rescontact')
                rescusine = form.cleaned_data.get('recusine')
                respic = form.respic
                restaurant = Restaurant(Res_Name=resname,Res_description=resdescription,Res_contact=rescontact,Res_cusine=rescusine,Res_Pic = respic)
                restaurant.save()
                user = User.objects.get(pk=(User.objects.get(username=request.user.username).id))
                user.userprofile.userRestaurant = Restaurant.objects.get(Res_Name=resname)
                user.save()
        else:
            RestaurantCreation()

def restaurantPage(request, restaurantName):
    resDetail = Restaurant.objects.get(Res_Name=restaurantName)
    return render(request, 'restaurant/restaurant.html', {'Restaurant':resDetail})

def createRestaurant(request):
    if request.method == 'POST':
        Restaurant_Name = request.POST['']
    return render(request, 'create-restaurant.html')

def processMenu(request):
    return render(request,'create-menu.html')

def createMenuItems(request):
    if request.method == 'POST':
        #Rest = request.POST['Rest']
        Menu_Item = request.POST['Item']
        
        Res = Restaurant.objects.get(Res_Name = request.POST['Rest'])
        Menu_Description = request.POST['Description']
        Menu_ItemPrice = request.POST["Price"]
        Name = request.POST['Label']
        #Cuisine_Type = request.POST.get('Cuisine', '')
        #Label_Name = request.POST.get('Label', '')
        itemCreate = Menu(Menu_Item = Menu_Item, Menu_ItemPrice = Menu_ItemPrice,
         Menu_Item_Description = Menu_Description, Menu_Res_Id = Res)
        itemCreate.save()
        labelCreate = Label(Label_Name = Name, Label_Menu_Id = itemCreate)
        labelCreate.save()
    #priceCreate = Menu.objects.create(Menu_ItemPrice = 0 )
    #descriptCreate = Menu.objects.create(Menu_Description = 'test')
    return render(request, 'create-menu.html')

def createLabel(request):
    labelCreate = Label.objects.create(Label_Name = '')


