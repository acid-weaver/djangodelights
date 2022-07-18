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
	# original_field = forms.CharField()
	# extra_field_count = forms.CharField(widget=forms.HiddenInput())

	def __init__(self, *args, **kwargs):
		super(PurchaseForm, self).__init__(*args, **kwargs)
		for i in MenuItem.objects.all():
			self.fields['{}'.format(i.id)] = forms.IntegerField(label=i.title)
	
	def clean(self):
		cleaned_data = super(PurchaseForm, self).clean()
		self.client = cleaned_data.get('client')
		dict = {}
		sum = 0
		for i in MenuItem.objects.all():
			dict[i.title] = cleaned_data.get('{}'.format(i.id))
			print(cleaned_data.get('{}'.format(i.id)))
			sum += dict[i.title]
		if sum == 0:
			raise forms.ValidationError('This purchase is empty')
		cleaned_data['menu_items'] = dict
		print(cleaned_data['menu_items'])

	menu_items = forms.JSONField(required=False, widget=forms.HiddenInput())
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