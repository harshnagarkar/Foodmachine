from django.shortcuts import render
from .models import User,UserProfile
from authentication.forms import SignUpForm
from django.http import HttpResponse

from django.http import HttpResponsePermanentRedirect
# Create your views here.

def home(request):
		return render(request, 'home.html')

def userView(request):
	# if request.user.is_authenticated():
	return render(request, 'dashboard/userdashboard.html')
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
			email = form.cleaned_data.get('Email')
			phone = form.cleaned_data.get('phone')
			print (username)

	else:
		form = SignUpForm()

	return render(request, 'cong.html', {"username" : username})
	#return HttpResponse(username)