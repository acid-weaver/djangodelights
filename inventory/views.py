from django.shortcuts import render
from django.views.generic import ListView
from .models import *

# Create your views here.
navigation = [
				# {'title':'Main', 'url_name':'main', 'icon':'home'},
				{'title':'Inventory', 'url_name':'inventory'},
			]

class WarehouseView(ListView):
	model = Ingredient
	template_name = 'inventory/inventory.html'
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['nav_menu'] = navigation
		return context

