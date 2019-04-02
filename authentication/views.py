from django.shortcuts import render
from .models import User,UserProfile
from authentication.forms import *
from django.http import HttpResponse
from .apps import userCreate,updatePassword
from django.contrib.auth.models import AnonymousUser

from django.http import HttpResponsePermanentRedirect,HttpResponseRedirect
# Create your views here.

def home(request):
		return render(request, 'home.html')

def userView(request):
	print (request.user)
	if request.user.is_authenticated:
		context = User.objects.get(pk=(User.objects.get(username=request.user.username).id))
		if context.userprofile.userType== 'c':
			return render(request, 'dashboard/Userdashboardnew.html')
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
			answer = form.cleaned_data.get('secAnswer')
			questions = form.cleaned_data.get('questions')
			# print(question)
			userCreate(UserName=username,Password=confirmpass,Email=email,First_Name=fname,Last_Name=lname,Answer = answer,Question=questions,UserType='c',UserRestaurant=None)
			

	else:
		form = SignUpForm()

	return render(request, 'cong.html', {"username" : username})


# def loginUser(request):
# 	if request.method == "POST":
# 		form = LoginForm(request.POST)
# 		print(form.errors)
# 		print(form.is_valid)
# 		if form.is_valid():
# 			username = form.cleaned_data.get('username')
# 			passw = form.cleaned_data.get('password')

# 			user = loginuser(request)
# 			print  (user)
# 			return render(request, 'dashboard/userdashboard.html')
# 		else:
# 			form = LoginForm()
		


	# return render(request, template_name, loginUser(request))
			# username = form.cleaned_data.get('username')
			# passw = form.cleaned_data.get('password')
			# user = loginuser(request)
		# 	loginUser(username, passw)
		# 	return render(request, 'userdashboard.html')
		# else:
		# 	form = LoginForm()
# def logUser(request):		
# 	context = request.POST
# 	if request.user.is_authenticated():
# 		return HttpResponse("Logged in")
# 	if request.method == 'POST':
# 		username = request.POST['username']
# 		password = request.POST['password']
# 		user = authenticate(username=username, password=password)
# 		print(user)
# 		if user:
# 			if user.is_active:
# 				login(request, user)
# 				return HttpResponse("Success")
# 			else:
# 				return HttpResponse("Not active")
# 		else:
# 			return HttpResponse("Invalid")
# 	else:
# 		return render(request, 'templates/logn.html', {}, context)
# def updatePass(request):

# 	if request.method == "POST":
# 		form = UpdatePassword(request.POST)
# 		print(form.error)
# 		if(form.is_valid()):
# 			confirmPass= form.cleaned_data.get('confirmPass')
# 			username = form.cleaned_data.get('username')
# 			updatePassword(username,confirmPass)
# 		else:
# 			form = UpdatePassword()
