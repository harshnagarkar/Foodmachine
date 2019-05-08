from django import forms
from django.contrib.auth.models import AbstractUser, User

class SignUpForm(forms.Form): 

    username = forms.CharField(label='username', max_length=100)
    FirstName = forms.CharField(label='FirstName', max_length = 100)
    LastName = forms.CharField(label = 'LastName', max_length = 100)
    passw = forms.CharField(widget=forms.PasswordInput)
    confirmPass = forms.CharField(widget=forms.PasswordInput)
    types = forms.CharField(max_length=1, label='what type are you?')
    Email = forms.EmailField( max_length=70)
    class Meta:
        model = User
        fields = ('username','Email','FirstName','LastName','passw', 'confirmPass')
        

class RestaurantForm(forms.Form):

    username = forms.CharField(label='username', max_length=100)
    FirstName = forms.CharField(label='FirstName', max_length=100)
    LastName = forms.CharField(label='LastName', max_length=100)
    passw = forms.CharField(widget=forms.PasswordInput)
    confirmPass = forms.CharField(widget=forms.PasswordInput)
    Email = forms.EmailField(max_length=70)
    usertype = forms.CharField(max_length=1)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email addresses already exsist.')
        return email

    class Meta:
        model = User
        fields = ('username', 'Email', 'FirstName', 'LastName',
                  'passw', 'confirmPass', 'questions', 'secAnswer')



class UpdatePassword(forms.Form):
    newPassword = forms.CharField(widget=forms.PasswordInput)
    confirmPassword = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('newPassword', 'confirmPassword')

class UpdateProfile(forms.Form):

    fName = forms.CharField(label='fName', max_length=100)
    lName = forms.CharField(label = 'lName', max_length = 100)
    uEmail = forms.EmailField(label = 'uEmail')
    uPhone = forms.CharField(label = 'uPhone')
    uAddress = forms.CharField(label = 'uAddress')
    uPayment = forms.CharField(label = 'uPayment')

    class Meta:
        model = User
        fields = ('fName', 'lName', 'uEmail', 'uPhone', 'uAdress', 'uPayment')