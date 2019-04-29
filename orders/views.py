from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from restaurant.models import *
from django.http import HttpResponseServerError
import ast
from django.http import JsonResponse
from orders.models import *
from restaurant.models import *
from django.shortcuts import redirect
from authentication.models import *

@csrf_exempt
def cartpricecalculator(request):
    count = 0
    responsedata ={}
    if request.method == 'POST':
        data = json.loads(request.body)
        # print(data)
        # print(data['MeatZZa'][1]['quantity'])
        total = 0
        mid = {}
        rid = ""
        for k,v in (data.items()):
            priceval, mig, rig = priceCalculator(k,v[1]['quantity'])
            if not rid:
                rid = rig
            else:
                if not rig == rid:
                    return HttpResponseServerError()
            total += priceval
        #     # mvdata = {mig:v}
            mid[k] = {v[1]['quantity']: priceval}
            # print(mid)
            print(k+" ",priceval)
        #   responsedata[k] = priceval
        tax = total*0.07
        request.session['pref'] =''
        request.session['mid'] = json.dumps(mid)
        request.session['rid'] =rid
        request.session['total'] = (total+tax)
        responsedata["Tax"] = tax
        responsedata["total"]=(total+tax) 
        print(total)
        print(mid)
    return JsonResponse(responsedata)


def priceCalculator(mit,quantity):
    menuitem = Menu.objects.get(Menu_Item=mit)
    price = float(menuitem.Menu_ItemPrice) * float(quantity)
    res = menuitem.Menu_Res_Id
    return price,menuitem.Menu_Item_Id,res.Res_Id
      
def databaseEntry(mig,rig,status,userorder,price,pref=""):
    res = Restaurant.objects.get(Res_Id = rig)
    user = User.objects.get(pk=(User.objects.get(username=userorder.username).id))
    order = Orders(Menu_Item=str(mig),Preferences=pref,Status=status,Restaurant_Id=res,user=userorder,Price=price, Payment=user.userprofile.Payment)
    order.save()
    return order.Order_Id

def checkoutpage(request):
    user = request.user
    user = User.objects.get(pk=(User.objects.get(username=request.user.username).id))
    if(user.userprofile.Payment != None and user.userprofile.Address != None and user.userprofile.Phone != None):
        return render(request, "orders/shoppinigCart.html", {'User': user})
    else:
        return render(request,'orders/datamissing.html')

def updatePref(request):
    if request.type =="POST":
        pref = json.loads(request.body)
        # id = pref[0]['orderno']
        #
        request.session['pref'] = pref['content']
        return HttpResponse('200 Okay')

def orderProcessing(request):
    user = User.objects.get(pk=(User.objects.get(username=request.user.username).id))
    if user.userprofile.userType == 'c':
        orderId = databaseEntry(mig=request.session['mid'],pref=request.session['pref'],rig=request.session['rid'],status='s',userorder=request.user,price=request.session['total'])
        rurl = '/cart/status/'+str(orderId)+"/"
        # subject = "You just placed an order right now"+str(orderId)
        # Message = "Your order has been submitted sucessfully. Your link to check status is \n"+ rurl
        # me = 'admin@foodmachine.ml'
        # to = request.user.email
        # send_mail(subject,Message,me,to,fail_silently=False)
        return redirect(rurl)
    else:
        return render(request,'orders/notorder.html')


def orderStatus(request,orderid):
    print(orderid)
    order = Orders.objects.get(Order_Id=orderid)
    if order.user == request.user:
        return render(request,'orders/status.html',{'order':order})
    else:
        return render(request,'404.html')