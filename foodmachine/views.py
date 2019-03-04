from django.shortcuts import render

# Create your views here.

def home(request):
		return render(request, 'home/home.html')

def forgotpassword(request):
	return(request,'/forgot_password/fors.html')
		