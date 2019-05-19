from .forms import SignUpForm
from django.shortcuts import render
from .models import User, UserProfile
from authentication.forms import *
from django.http import HttpResponse
from .apps import *
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.models import AnonymousUser
import os
from sendgrid.helpers.mail import *
import sendgrid
from django.http import HttpResponse
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from orders.models import *
from django.core.mail import send_mail
from django.shortcuts import redirect


def home(request):
    return render(request, 'home.html')


def userView(request):
    print(request.user)
    if not request.user.is_authenticated:
        redirect('/login/')
    try:
        if request.user.is_authenticated:
            context = User.objects.get(
                pk=(User.objects.get(username=request.user.username).id))

            if request.method == "POST":
                form = UpdateProfile(request.POST)
                print("form")
                print(form.errors)
                if form.is_valid():
                    context = User.objects.get(username=request.user.username)
                    profile = UserProfile.objects.get(user=request.user)
                    print("log1")
                    context.first_name = form.cleaned_data.get('fName')
                    print(context.first_name)
                    context.last_name = form.cleaned_data.get('lName')
                    context.email = form.cleaned_data.get('uEmail')
                    profile.Phone = "+1"+form.cleaned_data.get('uPhone')
                    profile.Address = form.cleaned_data.get('uAddress')
                    profile.Payment = form.cleaned_data.get('uPayment')
                    context.save()
                    profile.save()
                    return redirect('/dashboard/')
                else:
                    return redirect('/dashboard/')

            else:
                if context.userprofile.userType == 'c':
                    my = Orders.objects.filter(user=request.user)
                    return render(request, 'dashboard/Userdashboard.html', {'User': context, 'My': my})
                elif context.userprofile.userType == 'r':
                    res = context.userprofile.userRestaurant
                    context = Orders.objects.filter(
                        Restaurant_Id=res, Status='s') | Orders.objects.filter(Restaurant_Id=res, Status='r')
                    youorder = Orders.objects.filter(
                        Restaurant_Id=res, Status='d') | Orders.objects.filter(Restaurant_Id=res, Status='r')
                    return render(request, 'dashboard/Ownerdashboard.html', {'Orders': context, 'My': youorder})
                elif context.userprofile.userType == 'd':
                    context = Orders.objects.filter(Deliverer=None)
                    youorder = Orders.objects.filter(Deliverer=request.user)
                    return render(request, 'dashboard/deliverydashboard.html', {'Orders': context, 'My': youorder})

        else:
            HttpResponseRedirect("/login/")
    except:
        redirect('/login/')


def makeUser(request):
    username = "N/A"
    if request.method == "POST":
        form = SignUpForm(request.POST)
        print(form.errors)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            fname = form.cleaned_data.get('FirstName')
            lname = form.cleaned_data.get('LastName')
            passw = form.cleaned_data.get('pass')
            confirmpass = form.cleaned_data.get('confirmPass')
            email = form.cleaned_data.get('Email')
            types = form.cleaned_data.get('types')

            Emailuser = email
            print(Emailuser)

            userCreate(UserName=username, Password=confirmpass, Email=email,
                       First_Name=fname, Last_Name=lname, UserType=types, UserRestaurant=None)
            send_mail(
                'Food machine account created',
                'Thank you for making an account.'+username,
                'admin@foodmachine.ml',
                [email],
                fail_silently=False,
            )
            return render(request, 'cong.html', {"username": username})

    else:
        form = SignUpForm()
    print(form.errors)
    return render(request, 'cong.html', {"username": 'Username exsisted Sorry.'})

def updatePass(request):
    if request.method == "POST":
        form = UpdatePassword(request.POST)
        print(form.errors)
        if form.is_valid():
            passw = form.cleaned_data.get('confirmPass')

            updatePassword(request.user.username, passw)
            return redirect('/dashboard/updatePassword')
        else:
            return redirect('404.html')

    else:
        return render(request, 'dashboard/updatePassword.html')
