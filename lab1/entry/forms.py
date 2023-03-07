from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
	# POSITION_CHOICES = {
 #        ('secretary', 'Secretary'),
 #        ('associate director', 'Associate Director'),
 #        ('director', 'Director'),
 #    }
	email = forms.EmailField(required = True)
	name = forms.CharField(max_length = 50, required = True)
	surname = forms.CharField(max_length = 50, required = True)
	position = forms.CharField(max_length = 150, required = True)
	address = forms.CharField(max_length = 50, required = True)
	phone = forms.CharField(max_length = 14, required = True)

	class Meta:
		model = User
		fields = ("name", "surname", "position", "address", "phone", "username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(UserCreateForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.name = self.cleaned_data['name']
		user.surname = self.cleaned_data['surname']
		user.position = self.cleaned_data['position']
		user.address = self.cleaned_data['address']
		user.phone = self.cleaned_data['phone']
		if commit:
			user.save()
		return user