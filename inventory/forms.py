from email.policy import default
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *


class IngredientForm(forms.ModelForm):
	class Meta:
		model = Ingredient
		fields = '__all__'

class PurchaseForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(PurchaseForm, self).__init__(*args, **kwargs)
		for i in MenuItem.objects.all():	# adds an input int for each position in menu to generate JSON later
			self.fields['{}'.format(i.id)] = forms.IntegerField(label=i.title)
	
	def clean(self):
		cleaned_data = super(PurchaseForm, self).clean()
		menu_items = {}

		for i in MenuItem.objects.all():
			if cleaned_data.get('{}'.format(i.id)) != 0:
				menu_items[i.title] = cleaned_data.get('{}'.format(i.id))

		if not menu_items:
			raise forms.ValidationError('This purchase is empty')

		cleaned_data['menu_items'] = menu_items	# this would be saved to DB (if validation would be succeed)

	menu_items = forms.JSONField(required=False, widget=forms.HiddenInput())	# fake invisible field just to ModelForm methods save it to DB
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


class LoginUserForm(AuthenticationForm):
	username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'uk-input'}))
	password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'uk-input'}))