from django.shortcuts import render
from itertools import chain
# Create your views here.
from restaurant.models import Restaurant, Menu, Label, Review, Cuisine
from restaurant.forms import *
from django.http import HttpResponseRedirect,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from orders.models import *
# from .filters import CuisineFilter


def initialcreateRestaurant(request):
    return render(request,'restaurant/createRestaurant.html')

def createRestaurant(request):
     user = User.objects.get(pk=(User.objects.get(username=request.user.username).id))
     if (user.userprofile.userRestaurant!=None and user.userprofile.userType=='r'):
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

            cuisine = Cuisine.objects.get(Cuisine_parent=form.cleaned_data.get('Cuisine'))
            respic = form.cleaned_data.get('Picture')
            Description = form.cleaned_data.get('Description')
            Price = form.cleaned_data.get('Price')
            CuisineName = form.cleaned_data.get('Cuisine')
            Labelname = form.cleaned_data.get('Label')
            exist = Label.objects.filter(Label_Name = Labelname).exists()
            if(exist == False):
                labelCreate = Label(Label_Name=Labelname)
                labelCreate.save()

            labelId = Label.objects.get(Label_Name=Labelname)
            itemCreate = Menu(Menu_Item=Item, Menu_ItemPrice=Price,Menu_Item_Description=Description,Menu_Cuisine=cuisine,Menu_Pic = respic,Menu_Label_Id=labelId, Menu_Res_Id=Rest)
            itemCreate.save()
      
        return redirect("/restaurant/createmenu/")
       
     else:
        return render(request, 'create-menu.html')

def restaurantPage(request, restaurantName):
    # resDetail = get_object_or_404(Restaurant, Res_Name=restaurantName)
    resDetail = get_object_or_404(Restaurant, Res_Name=restaurantName)
    if request.user.is_authenticated:
         user = User.objects.get(pk=(User.objects.get(username=request.user.username).id))
         if(user.userprofile.userRestaurant==Restaurant.objects.get(Res_Name=restaurantName)):
            return render(request, 'restaurant/restaurants.html', {'Restaurant':resDetail})
         else:
            return render(request, 'restaurant/nonadminsinglerestaurant.html', {'Restaurant':resDetail})
    else:
        return render(request,'restaurant/nonadminsinglerestaurant.html',{'Restaurant':resDetail})

def processMenu(request):
    return render(request,'create-menu.html')



def menuDelete(request, part_id = None):
    objects = Menu.objects.get(Menu_Item_Id=part_id)
    user = User.objects.get(pk=(User.objects.get(username=request.user.username).id))
    resobject = objects.Menu_Res_Id
    if(resobject==user.userprofile.userRestaurant):
        objects.delete()
        restaurantname = "/restaurant/"+resobject.Res_Name
        return redirect(restaurantname)
    else:
        return HttpResponse("This is not your restaurant")


def menuEdit(request, part_id = None):
    if request.method == 'POST':
        form = MenuCreation(request.POST, request.FILES)
        user = User.objects.get(pk = (User.objects.get(username = request.user.username).id))
        obj = Menu.objects.get(Menu_Item_Id = part_id)
        resObj = obj.Menu_Res_Id
        if(resObj == user.userprofile.userRestaurant):
            if(form.is_valid()):
                obj.Menu_Item = form.cleaned_data.get('Item')
                obj.Menu_ItemPrice = form.cleaned_data.get('Price')
                obj.Menu_Item_Description = form.cleaned_data.get('Description')
                
                lblName = form.cleaned_data.get('Label')
                exist = Label.objects.filter(Label_Name = lblName).exists()
                if(exist == False):
                    labelCreate = Label(Label_Name=Labelname)
                    labelCreate.save()

                lbl = Label.objects.get(Label_Name = lblName)
                obj.Menu_Label_Id = lbl
                # if(form.cleaned_data.get('Cuisine')!=None):
                obj.Menu_Cuisine = Cuisine.objects.get(Cuisine_parent = form.cleaned_data.get('Cuisine'))

                obj.save()
            url = '/restaurant/'+str(resObj.Res_Name)
            return redirect(url)

    else:
        obj = Menu.objects.get(Menu_Item_Id = part_id)
        resObj = obj.Menu_Res_Id
        return render(request, 'updateMenu.html',{'M':obj})




def updateStatus(request):
    status = Orders.objects.get()
    if request.method == 'POST':
         user = User.objects.get(pk=(User.objects.get(username=request.user.username).id))
         res = user.userprofile.userRestaurant
         orderno = request.POST.get('on')
         order = Orders.objects.get(Order_Id=orderno)
         order.Status = request.POST.status
         order.save()

def restList(request):

   
    #form = RestList(request.POST, request.FILES)
    #Cuis_list = Cuisine.objects.all()
        # = CuisineFilter(request.GET, queryset = Cuis_list)
    cuis = request.GET.get('Cuisine')
    qs = Restaurant.objects.all()
    cuisId = Cuisine.objects.get(Cuisine_parent = cuis)
    #comparison = qs.values('Cuisine_Type')
    comparison = qs.filter(Cuisine_Type = cuisId).values('Cuisine_Type')
    print(cuisId)
    print(comparison)
    try:
        if  cuisId != '' and cuis is not None:
            print("Success")
            qs = qs.filter(Cuisine_Type = cuisId)
        else:
            qs = qs
            print("Test")
    except:
        print("Error")


    # print(request.GET.get('sort'))
    # if(request.GET.get('sort')):
       
    #     qs = qs.order_by('Res_Name')
    #     print ("Did it work?")

    
    # for i in qs.order_by('Res_Name'):
    #     print(i)
        
    context = { 'query_set': qs}
    return render(request, 'restaurant/rest-list.html', context)


def foodList(request):

    lab = request.GET.get('Label')
    qs = Menu.objects.all()
    try:
        labId = Label.objects.get(Label_Name=lab)
        print(labId)
        if labId != '' and lab is not None:
            qs = qs.filter(Menu_Label_Id = labId)
        else:
            qs = qs
    except:
        print("Error")
    context = {'query_set' : qs}
    return render(request, 'restaurant/food-list.html', context)

