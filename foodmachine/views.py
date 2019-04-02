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

def testView(request):
    return render(request, 'test/test.html')  

# Attempted reset password.
def password_reset(request):
	return render (request, 're.html')

def register(request):
    return render(request, 'sgnup.html')

def reset(request):
    return render(request, 're.html')

def forgot(request):
    return render(request, 'for.html')

# Attempted signup. So far, doesn't work.
#class SignUp(generic.CreateView):
 #   form_class = UserCreationForm
  #  success_url = reverse_lazy('login')
   # template_name = 'sgnup.html'

def sendEmail(request):
    sg = sendgrid.SendGridAPIClient(apikey= send_key)
    from_email = Email("admin@foodmachine.ml")
    to_email = Email("ragrawa1@go.olemiss.edu")
    subject = "Sending with SendGrid is Fun"
    content = Content("text/plain", "and easy to do anywhere, even with Python")
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
