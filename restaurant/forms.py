from django import forms


class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')
		
class ProfileForm(forms.ModelForm)
	class Meta:
		model = UserProfile
		fields = ('phone', 'gender')

class MenuCreation(forms.ModelForm):
	class Meta:
		model = Menu
		fields = ('Item', 'Price', 'Description')

class LabelCreation(forms.ModelForm):
	class Meta:
		models = Label
		fields = ('Label')
class RestaurantCreation(form.ModelForm):
	resname = forms.CharField(label='RestaurantName', max_length=100)
	resdescription= forms.CharField(max_length=150,null=True)
	rescontact = forms.CharField(max_length=10)
	resaddress= forms.CharField(max_length=75)
	rescusine = forms.CharField(max_length=25,required=False)
	respic = forms.ImageField(help_text="Upload image: ", required=False)
	class Meta:
		model = Restaurant
		fields = ('resname','resdescription','rescontact','resaddress','recusine','respic')
