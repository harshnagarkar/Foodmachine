from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.

def home(request):
	return render(request, 'home.html')

#def forgotpassword(request):
#	return(request,'/forgot_password/fors.html')
		
