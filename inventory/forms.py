from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *


class IngredientCreateForm(forms.ModelForm):
	class Meta:
		model = Ingredient
		fields = '__all__'


class IngredientUpdateForm(forms.ModelForm):
	class Meta:
		model = Ingredient
		fields = '__all__'


class PurchaseCreateForm(forms.ModelForm):
	class Meta:
		model = Purchase
		fields = '__all__'


class RegisterUserForm(UserCreationForm):
	username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'uk-input'}))
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'uk-input'}))
	password2 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'uk-input'}))
	class Meta:
		model = User
		fields = ('username', 'password1', 'password2')
		# widgets = {
		# 	'username': forms.TextInput(attrs={'class': 'uk-input'}),
		# 	'password1': forms.PasswordInput(attrs={'class': 'uk-input'}),
		# 	'password2': forms.PasswordInput(attrs={'class': 'uk-input'}),
		# }


class LoginUserForm(AuthenticationForm):
	username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'uk-input'}))
	password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'uk-input'}))