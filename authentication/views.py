from django.shortcuts import render

# Create your views here.

def home(request):
		return render(request, 'home.html')
		#return render(request, 'loginPageIndex.html')
		
#def log(request):
#		return render(request, 'loginPageIndex.html')
#def password_reset(request):
#		return render(request, 'home.html')