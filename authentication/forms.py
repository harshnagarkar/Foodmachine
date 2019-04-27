from django import forms
#from .models import Post
from django.contrib.auth.models import AbstractUser, User

class SignUpForm(forms.Form): 

    username = forms.CharField(label='username', max_length=100)
    FirstName = forms.CharField(label='FirstName', max_length = 100)
    LastName = forms.CharField(label = 'LastName', max_length = 100)
    passw = forms.CharField(widget=forms.PasswordInput)
    confirmPass = forms.CharField(widget=forms.PasswordInput)
    types = forms.CharField(max_length=1, label='what type are you?')
    Email = forms.EmailField( max_length=70)
    # phone = forms.CharField(max_length=10)
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

# class LoginForm(forms.Form):

#     username = forms.CharField(label='username', max_length=100)
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ('username','password')

class UpdatePassword(forms.Form):

    # oldPassword = forms.CharField(widget=forms.PasswordInput)
    newPassword = forms.CharField(widget=forms.PasswordInput)
    confirmPassword = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('newPassword', 'confirmPassword')

# class ForgotPassword(forms.Form):

