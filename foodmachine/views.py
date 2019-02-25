from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.

def home(request):
		return render(request, 'home.html')
		#return render(request, 'loginPageIndex.html')

# Attempted reset password.
#def password_reset(request):
#		return render (request, 're.html')

# Attempted signup. So far, doesn't work.
#class SignUp(generic.CreateView):
 #   form_class = UserCreationForm
  #  success_url = reverse_lazy('login')
   # template_name = 'sgnup.html'