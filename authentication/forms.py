from django import forms
#from .models import Post

class SignUpForm(forms.Form): 
    username = forms.CharField(label='Username', max_length=100)
    first = forms.CharField(label='FirstName', max_length = 100)
    last = forms.CharField(label = 'LastName', max_length = 100)
    password = forms.PasswordInput()
    email = forms.EmailField(label = 'email')
    phone = forms.CharField(label='phone', max_length = 10)
