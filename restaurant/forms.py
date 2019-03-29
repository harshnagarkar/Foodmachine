from django import forms
from authentication.models import *
from django.contrib.auth.models import User, AbstractUser
from restaurant.models import *

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')
		
class MenuCreation(forms.ModelForm):
	class Meta:
		model = Menu
		fields = ('Menu_Item', 'Menu_ItemPrice', 'Menu_Item_Description')

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
