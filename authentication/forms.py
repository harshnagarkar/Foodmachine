from django import forms
#from .models import Post
from django.contrib.auth.models import AbstractUser, User

class SignUpForm(forms.Form): 

    username = forms.CharField(label='username', max_length=100)
    FirstName = forms.CharField(label='FirstName', max_length = 100)
    LastName = forms.CharField(label = 'LastName', max_length = 100)
    passw = forms.CharField(widget=forms.PasswordInput)
    Email = forms.EmailField( max_length=70)
    phone = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ('username','Email','phone','FirstName','LastName','passw')
        # widgets = {
        #     # telling Django your password field in the mode is a password input on the template
        #     'password': forms.PasswordInput()
        # }
        
    # email = forms.EmailField(label = 'email')
    # phone = forms.CharField(label='phone', max_length = 10)

    # def clean(self):
    #     cleaned_data = super().clean()
    #     username = cleaned_data.get("username")
    #     first = cleaned_data.get("first")
