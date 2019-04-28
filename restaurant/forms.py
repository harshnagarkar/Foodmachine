from django import forms
from authentication.models import *
from django.contrib.auth.models import User, AbstractUser
from restaurant.models import *

class UserForm(forms.Form):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')
		
class MenuCreation(forms.Form):
	# Rest = forms.CharField(label = 'Rest', max_length = 75)
	Item = forms.CharField(label = 'Item', max_length = 50)
	Description = forms.CharField(label = 'Description', max_length = 100)
	Price = forms.DecimalField(label = 'Price', max_digits = 30, decimal_places = 2)
	Cuisine = forms.CharField(label = 'Cuisine', max_length = 20, required = False)
	Label = forms.CharField(max_length = 20, required = True)
	Picture = forms.ImageField(label = 'Picture', help_text = "Upload image: ", required = False)

	class Meta:
		model = Menu
		fields = ('Item', 'Description', 'Price', 'Cuisine', 'Label', 'Picture')

class MenuUpdate(forms.Form):

	Item = forms.CharField(label = 'Item', max_length = 50)
	Description = forms.CharField(label = 'Description', max_length = 100)
	Price = forms.DecimalField(label = 'Price', max_digits = 30, decimal_places = 2)
	Cuisine = forms.CharField(label = 'Cuisine', max_length = 20, required = False)
	Label = forms.CharField(max_length = 20, required = True)
	Picture = forms.ImageField(label = 'Picture', help_text = "Upload image: ", required = False)

	class Meta:
		model = Menu
		fields = ('Item', 'Description', 'Price', 'Cuisine', 'Label', 'Picture')
	



# class LabelCreation(forms.ModelForm):
# 	class Meta:
# 		models = Label
# 		fields = ('Label_Name')


class RestaurantCreation(forms.Form):

	resname = forms.CharField(label='RestaurantName', max_length=100)
	resdescription= forms.CharField(max_length=150,required=False)
	rescontact = forms.CharField(max_length=10)
	resaddress= forms.CharField(max_length=75)
	rescusine = forms.CharField(max_length=25,required=False)
	respic = forms.ImageField(help_text="Upload image: ", required=False)
	class Meta:
		model = Restaurant
		fields = ('resname','resdescription','rescontact','resaddress','recusine','respic')

class RestList(forms.Form):

	cuisine = forms.CharField(max_length = 20)
	class Meta:
		model = Cuisine
		fields = ('cuisine')