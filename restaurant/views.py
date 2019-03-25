from django.shortcuts import render
from itertools import chain
# Create your views here.
from .models import Restaurant,Menu,Cuisine,Review, Label


def restaurantPage(request, restaurantName):
    resDetail = Restaurant.objects.get(Res_Name=restaurantName).__dict__
    return render(request, 'restaurant/restaurant.html', resDetail)

def createRestaurant(request):
    if request.method == 'POST':
        Restaurant_Name = request.POST['']
    return render(request, 'create-restaurant.html')

def processMenu(request):

    print (request.POST)
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

# def createLabel(request):
#     labelCreate = Label.objects.create(Label_Name = '')


