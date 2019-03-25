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