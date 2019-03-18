from django.shortcuts import render
from .models import User,UserProfile
from django.http import HttpResponseRedirect
from django.http import HttpResponsePermanentRedirect
# Create your views here.

def home(request):
		return render(request, 'home.html')

def userView(request):
	# if request.user.is_authenticated():
	return render(request, 'dashboard/userdashboard.html')
	# else:
		# return HttpResponsePermanentRedirect("/login")
