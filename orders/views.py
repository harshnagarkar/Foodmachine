from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from restaurant.models import *
# import ast
@csrf_exempt
def cartpricecalculator(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # data = data.dict()
        total = 0
        mid = ""
        rid = ""
        for k,v in (data.items()):
            priceval, mig, rig = priceCalculator(k,v)
            total += priceval
            mid = mid+ str(mig)+", "
            rid = rid+ str(rig)+", "
            print(k+" ",priceval)
        tax = total*0.07
        print("Tax" , tax)
        print("total",(total+tax) )
        print(mid)
        print(rid)

    return HttpResponse('200 Okay')


def priceCalculator(mit,quantity):
    menuitem = Menu.objects.get(Menu_Item=mit)
    price = float(menuitem.Menu_ItemPrice) * float(quantity)
    res = menuitem.Menu_Res_Id
    return price,menuitem.Menu_Item_Id,res.Res_Id
      
# def databaseEntry(mig,pref="",rig):

