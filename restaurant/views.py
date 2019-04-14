from django.shortcuts import render
from itertools import chain
# Create your views here.
from restaurant.models import Restaurant,Menu,Label,Review
from restaurant.forms import *
from django.http import HttpResponseRedirect
# from django.shortcuts import get_object_or_404
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
                user.userprofile.userRestaurant = Restaurant.objects.get(userType='r')
                user.save()
        else:
             return HttpResponseRedirect("/restaurant/createRestaurant/")


def createMenuItems(request):
     if request.method == 'POST':
        form = MenuCreation(request.POST, request.FILES)
        print(form.errors)
        user = User.objects.get(
            pk=(User.objects.get(username=request.user.username).id))
        if form.is_valid():
            Item = form.cleaned_data.get('Item')
            resname = user.userprofile.userRestaurant
            print(resname)
            Rest = resname
            # Rest = Restaurant.objects.only('Res_Id').get(Res_Name = form.cleaned_data.get('Rest')).id

            Description = form.cleaned_data.get('Description')
            Price = form.cleaned_data.get('Price')
            Labelname = form.cleaned_data.get('Label')
            labelCreate = Label(Label_Name=Labelname)
            labelCreate.save()
            labelId = Label.objects.get(Label_Name=Labelname)
            itemCreate = Menu(Menu_Item=Item, Menu_ItemPrice=Price,Menu_Item_Description=Description, Menu_Label_Id=labelId, Menu_Res_Id=Rest)
            itemCreate.save()

        return render(request, 'createdmenu.html')
     else:
        return render(request, 'create-menu.html')

def restaurantPage(request, restaurantName):
    # resDetail = get_object_or_404(Restaurant, Res_Name=restaurantName)
    resDetail = Restaurant.objects.get(Res_Name=restaurantName)
    menuDetail = Menu.objects.filter(Menu_Res_Id=resDetail)
    return render(request, 'restaurant/restaurants.html', {'Restaurant':resDetail},{'Menu':menuDetail})

def processMenu(request):
    return render(request,'create-menu.html')



def createLabel(request):
    labelCreate = Label.objects.create(Label_Name = '')


