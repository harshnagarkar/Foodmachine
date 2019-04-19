from django.shortcuts import render
from itertools import chain
# Create your views here.
from restaurant.models import Restaurant,Menu,Label,Review,Cuisine
from restaurant.forms import *
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404


def initialcreateRestaurant(request):
    return render(request,'restaurant/createRestaurant.html')

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
                respic = form.cleaned_data.get('respic')
                resaddress = form.cleaned_data.get('resaddress')
                checkcuisine = ""
                try:
                    checkcuisine = Cuisine.objects.get(Cuisine_parent=rescusine)
                except:
                    newCuisine =Cuisine(Cuisine_parent=rescusine)
                    newCuisine.save()
                    checkcuisine = Cuisine.objects.get(Cuisine_parent=rescusine)
                restaurant = Restaurant(Res_Name=resname, Res_Description=resdescription, Res_Contact=('+1'+rescontact), Res_Address=resaddress, Cuisine_Type=checkcuisine, Res_Pic=respic)
                print(restaurant)
                restaurant.save()
                userobject = UserProfile.objects.get(user=request.user)
                userobject.userType = 'r'
                userobject.userRestaurant = Restaurant.objects.get(Res_Name=resname)
                userobject.save()
                return HttpResponseRedirect("/restaurant/"+resname)
            else:
                return redirect("/restaurant/createRestaurant/",{'form':form})
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
            #print(resname)
            Rest = resname
            # Rest = Restaurant.objects.only('Res_Id').get(Res_Name = form.cleaned_data.get('Rest')).id

            Description = form.cleaned_data.get('Description')
            Price = form.cleaned_data.get('Price') 
            Labelname = form.cleaned_data.get('Label')
            exist = Label.objects.filter(Label_Name = Labelname).exists()
            if(exist == False):
                labelCreate = Label(Label_Name=Labelname)
                labelCreate.save()
            
            labelId = Label.objects.get(Label_Name=Labelname)
            itemCreate = Menu(Menu_Item=Item, Menu_ItemPrice=Price,Menu_Item_Description=Description, Menu_Label_Id=labelId, Menu_Res_Id=Rest)
            itemCreate.save()
            
       
        return redirect("/restaurant/createmenu/")
       
     else:
        return render(request, 'create-menu.html')

def restaurantPage(request, restaurantName):
    # resDetail = get_object_or_404(Restaurant, Res_Name=restaurantName)
    resDetail = get_object_or_404(Restaurant, Res_Name=restaurantName)
    for key,value in request.session.items():
        print (key+" ->"+value)
    return render(request, 'restaurant/restaurants.html', {'Restaurant':resDetail})

def processMenu(request):
    return render(request,'create-menu.html')


# @csrf_exempt
# def menuDelete(request):
#     if request.method == "POST":
#         # Menu.objects.filter(id = )

def menuDelete(request, part_id = None):
    object = Menu.objects.get(Menu_Item_Id=part_id)
    resobject = object.Menu_Res_Id
    object.delete()
    restaurantname = "/restaurant/"+resobject.Res_Name
    return redirect(restaurantname)