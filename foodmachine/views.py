from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
import SENDGRIDkey
import sendgrid
import os
from sendgrid.helpers.mail import *
from django.views import generic
# Create your views here.

def home(request):
	return render(request, 'home.html')


