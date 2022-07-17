# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from .models import *
from .forms import *
from .utils import *


# Create your views here.
class WarehouseView(DataMixin, ListView):
	model = Ingredient
	template_name = 'inventory/inventory.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		mixin_context = self.get_user_context(title='Inventory', select=1)

		return dict(list(context.items()) + list(mixin_context.items()))


class MenuView(DataMixin, ListView):
	model = MenuItem
	template_name = 'inventory/menu.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		mixin_context = self.get_user_context(title='Menu', select=0)

		return dict(list(context.items()) + list(mixin_context.items()))


class PurchaseView(DataMixin, ListView):
	model = Purchase
	template_name = 'inventory/purchase.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		mixin_context = self.get_user_context(title='Purchases', select=2)

		return dict(list(context.items()) + list(mixin_context.items()))


class IngredientCreateView(DataMixin, CreateView):
	model = Ingredient
	form_class = IngredientCreateForm
	template_name = 'inventory/create_ingredient.html'
	success_url = reverse_lazy('inventory')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		mixin_context = self.get_user_context(title='Add Ingredient', select=1)

		return dict(list(context.items()) + list(mixin_context.items()))


class PurchaseCreateView(DataMixin, CreateView):
	model = Purchase
	form_class = PurchaseCreateForm
	template_name = 'inventory/create_purchase.html'
	success_url = reverse_lazy('purchase')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		mixin_context = self.get_user_context(title='Add Ingredient', select=1)

		return dict(list(context.items()) + list(mixin_context.items()))


class FinanceView(DataMixin, TemplateView):
	template_name = 'inventory/bookkeeping.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		profit = 0
		for p in Purchase.objects.all():
			profit += p.total_price
		context['total_profit'] = profit
		mixin_context = self.get_user_context(title='Bookkeeping', select=3)

		return dict(list(context.items()) + list(mixin_context.items()))


class RegisterUserView(DataMixin, CreateView):
	form_class = RegisterUserForm
	template_name = 'inventory/registration.html'
	success_url = reverse_lazy('menu')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		mixin_context = self.get_user_context(title='Registration')

		return dict(list(context.items()) + list(mixin_context.items()))
