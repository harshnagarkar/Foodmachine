from django.shortcuts import render
from itertools import chain
# Create your views here.
from .models import *
from restaurant.forms import *

def createRestaurant(request):
     user = User.objects.get(pk=(User.objects.get(username=request.user.username).id))
     if (user.userprofile.userRestaurant!=None):
         return render(request,'restaurant/restaurantProblem.html')
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
                respic = form.clean_data('respic')
                restaurant = Restaurant(Res_Name=resname,Res_description=resdescription,Res_contact=rescontact,Res_cusine=rescusine,Res_Pic = respic)
                restaurant.save()
                user.userprofile.userRestaurant = Restaurant.objects.get(Res_Name=resname)
                user.save()
        else:
             return HttpResponseRedirect("/restaurant/createRestaurant/")

def restaurantPage(request, restaurantName):
    resDetail = Restaurant.objects.get(Res_Name=restaurantName)
    menuDetail = Menu.objects.filter(Menu_Res_Id=resDetail)
    return render(request, 'restaurant/restaurants.html', {'Restaurant':resDetail},{'Menu':menuDetail})

def processMenu(request):
    return render(request,'create-menu.html')

def createMenuItems(request):
    if request.method == 'POST':
        #Rest = request.POST['Rest']
        form = MenuCreation()
        Menu_Item = request.POST['Item']
        Res = form.cleaned_data.get('Rest')
        Menu_Description = request.POST['Description']
        Menu_ItemPrice = request.POST["Price"]
        Name = request.POST['Label']
        
        #Cuisine_Type = request.POST.get('Cuisine', '')
        #Label_Name = request.POST.get('Label', '')
        labelCreate = Label(Label_Name = Name)
        labelCreate.save()
        lab = Label.objects.get(Label_Name = request.POST['Label'])
        itemCreate = Menu(Menu_Item = Menu_Item, Menu_ItemPrice = Menu_ItemPrice,
        Menu_Item_Description = Menu_Description, Menu_Label_Id = lab, Menu_Res_Id = Res)
        itemCreate.save()
    #priceCreate = Menu.objects.create(Menu_ItemPrice = 0 )
    #descriptCreate = Menu.objects.create(Menu_Description = 'test')
    return render(request, 'create-menu.html')

def createLabel(request):
    labelCreate = Label.objects.create(Label_Name = '')


