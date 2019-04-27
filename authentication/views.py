from django.shortcuts import render
from .models import User,UserProfile
from authentication.forms import *
from django.http import HttpResponse
from .apps import *
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.models import AnonymousUser
import os
from sendgrid.helpers.mail import *
import sendgrid
from django.http import HttpResponse
from django.http import HttpResponsePermanentRedirect,HttpResponseRedirect
from authentication.tests import emails
# Create your views here.
from django.shortcuts import redirect
def home(request):
		return render(request, 'home.html')

def userView(request):
	print (request.user)
	if request.user.is_authenticated:
		context = User.objects.get(pk=(User.objects.get(username=request.user.username).id))

		if request.method == "POST":
			form = UpdateProfile(request.POST)
			print("form")
			print(form.errors)
			if form.is_valid():
				context.first_name = form.cleaned_data.get('fName')
				context.last_name = form.cleaned_data.get('lName')
				context.email = form.cleaned_data.get('uEmail')
				context.userprofile.Phone = "+1"+form.cleaned_data.get('uPhone')
				context.userprofile.Address = form.cleaned_data.get('uAddress')
				context.userprofile.Payment = form.cleaned_data.get('uPayment')

				context.save()
				context.userprofile.save()
				return redirect('/dashboard/')
			else:
				return redirect('/dashboard/')

		else:
			if context.userprofile.userType== 'c':
				return render(request, 'dashboard/Userdashboard.html')
			elif context.userprofile.userType == 'r':
				return render(request, 'dashboard/restaurantdashboard.html')
			elif context.userprofile.userType == 'd':
				return render(request, 'dashboard/deliverydashboard.html')

	else:
		HttpResponseRedirect("/")
	# else:
		# return HttpResponsePermanentRedirect("/login")

from .forms import SignUpForm
#class SignUpView():
#	template_name = 'templates/sgnup.html'
# form = SignUpForm(request.POST)

def makeUser(request):
	username = "N/A"
	if request.method == "POST":	
		form = SignUpForm(request.POST)
		print (form.errors)
		print (form.is_valid())
		if form.is_valid():
			username = form.cleaned_data.get('username')
			fname = form.cleaned_data.get('FirstName')
			lname = form.cleaned_data.get('LastName')
			passw = form.cleaned_data.get('pass')
			confirmpass = form.cleaned_data.get('confirmPass')
			email = form.cleaned_data.get('Email')
			types = form.cleaned_data.get('types')
			# answer = form.cleaned_data.get('secAnswer')
			# questions = form.cleaned_data.get('questions')
			Emailuser = email
			print (Emailuser)
			# print(question)
			userCreate(UserName=username,Password=confirmpass,Email=email,First_Name=fname,Last_Name=lname,UserType=types,UserRestaurant=None)
			emails(email)
			return render(request, 'cong.html', {"username": username})
		

	else:
		form = SignUpForm()
	print (form.errors)
	return render(request, 'cong.html', {"username" : 'Username exsisted Sorry.'})


# def restaurantUser(request):
# 	# context = User.objects.get(pk=(User.objects.get(username=request.user.username).id))
# 	if request.method == "POST":
# 		form = RestaurantForm(request.POST)
# 		print(form.errors)
# 		print(form.is_valid())
# 		if form.is_valid():
# 			username = form.cleaned_data.get('username')
# 			fname = form.cleaned_data.get('FirstName')
# 			lname = form.cleaned_data.get('LastName')
# 			passw = form.cleaned_data.get('pass')
# 			confirmpass = form.cleaned_data.get('confirmPass')
# 			email = form.cleaned_data.get('Email')
# 			answer = form.cleaned_data.get('secAnswer')
# 			questions = form.cleaned_data.get('questions')
# 			usertype = form.cleaned_data('usertype')
# 			# print(question)
# 			restaurantUserCreate(UserName=username, Password=confirmpass, Email=email, First_Name=fname,Last_Name=lname, Answer=answer, Question=questions, UserType=usertype, UserRestaurant=None)

# 	else:
# 		form = RestaurantForm()

# 	return render(request, 'restaurant/sucessRestaurant.html', {"username": request.user.username})


def sendEmail(request):

	if request.method == "POST":
		form = ForgotPassword(request.POST)
		print(form.errors)
		print(form.is_valid())
		if form.is_valid():
			email = form.cleaned_data.get('email')
			u = verifyEmail(email)
			if u != None:
				sg = sendgrid.SendGridAPIClient( apikey='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')
				from_email = Email("admin@foodmachine.ml")
				to_email = Email(email)
				subject = "Request to Reset Password for Food Machine"
				content = Content(
                                    "text/plain", "and easy to do anywhere, even with Python")
				mail = Mail(from_email, subject, to_email, content)
				response = sg.client.mail.send.post(request_body=mail.get())

			else:
				return 'Email does not exist. Please try again!'

	else:
		form = ForgotPassword()

	return render(request, 'password_reset_confirm.html')

def updatePass(request):
	if request.method == "POST":
		form = UpdatePassword(request.POST)
		print(form.errors)
		if form.is_valid():
			passw = form.cleaned_data.get('confirmPass')
			
			updatePassword(request.user, passw)
			return redirect('/dashboard/updatePassword')

	else:
		return render(request, 'dashboard/updatePassword.html')
			


# 	if request.method == "POST":
# 		form = UpdatePassword(request.POST)
# 		print(form.error)
# 		if(form.is_valid()):
# 			confirmPass= form.cleaned_data.get('confirmPass')
# 			username = form.cleaned_data.get('username')
# 			updatePassword(username,confirmPass)
# 		else:
# 			form = UpdatePassword()
