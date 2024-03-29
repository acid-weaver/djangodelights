from django.http import HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *
from .utils import *


# Create your views here.
class MenuView(DataMixin, ListView):
	model = MenuItem
	template_name = 'inventory/menu.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		mixin_context = self.get_user_context(title='Menu', select=0)

		return dict(list(context.items()) + list(mixin_context.items()))


class WarehouseView(LoginRequiredMixin, DataMixin, ListView):
	model = Ingredient
	template_name = 'inventory/inventory.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		mixin_context = self.get_user_context(title='Inventory', select=1)

		return dict(list(context.items()) + list(mixin_context.items()))


class PurchaseView(LoginRequiredMixin, DataMixin, ListView):
	model = Purchase
	template_name = 'inventory/purchase.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		mixin_context = self.get_user_context(title='Purchases', select=2)

		return dict(list(context.items()) + list(mixin_context.items()))


class FinanceView(LoginRequiredMixin, DataMixin, TemplateView):
	template_name = 'inventory/bookkeeping.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		revenue = 0
		expenses = 0
		for p in Purchase.objects.all():
			expenses += p.total_expenses
			revenue += p.total_price
		context['total_revenue'] = revenue
		context['total_expenses'] = expenses
		context['total_profit'] = revenue - expenses
		mixin_context = self.get_user_context(title='Bookkeeping', select=3)

		return dict(list(context.items()) + list(mixin_context.items()))


class IngredientCreateView(LoginRequiredMixin, DataMixin, CreateView):
	model = Ingredient
	form_class = IngredientForm
	template_name = 'inventory/create_ingredient.html'
	success_url = reverse_lazy('inventory')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		mixin_context = self.get_user_context(title='Add Ingredient', select=1)

		return dict(list(context.items()) + list(mixin_context.items()))


class PurchaseCreateView(LoginRequiredMixin, DataMixin, CreateView):
	model = Purchase
	form_class = PurchaseForm
	template_name = 'inventory/create_purchase.html'
	success_url = reverse_lazy('purchase')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['menu_items'] = MenuItem.objects.all()
		mixin_context = self.get_user_context(title='Add Ingredient', select=2)

		return dict(list(context.items()) + list(mixin_context.items()))
	
	def form_valid(self, form):
		form.instance.client = self.request.user
		res = super().form_valid(form)
		form.instance.modify_inventory					# we already checked in PurchaseForm.clean() that we have enough ingredients, now we can modify their quantity after this purchase	
		form.save()

		return res


class IngredientUpdateView(LoginRequiredMixin, DataMixin, UpdateView):
	model = Ingredient
	form_class = IngredientForm
	template_name = 'inventory/update_ingredient.html'
	success_url = reverse_lazy('inventory')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		mixin_context = self.get_user_context(title='Add Ingredient', select=1)

		return dict(list(context.items()) + list(mixin_context.items()))


class PurchaseDeleteView(LoginRequiredMixin, DataMixin, DeleteView):
	model = Purchase
	template_name = 'inventory/delete_confirm.html'
	success_url = reverse_lazy('purchase')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		mixin_context = self.get_user_context(title='Add Purchase', select=2)

		return dict(list(context.items()) + list(mixin_context.items()))


class IngredientDeleteView(LoginRequiredMixin, DataMixin, DeleteView):
	model = Ingredient
	template_name = 'inventory/delete_confirm.html'
	success_url = reverse_lazy('inventory')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		mixin_context = self.get_user_context(title='Add Ingredient', select=1)

		return dict(list(context.items()) + list(mixin_context.items()))

# User functionality views:
class RegisterUser(DataMixin, CreateView):
	form_class = RegisterUserForm
	template_name = 'inventory/registration.html'
	success_url = reverse_lazy('menu')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		mixin_context = self.get_user_context(title='Registration')

		return dict(list(context.items()) + list(mixin_context.items()))
	
	def form_valid(self, form):	# login to account after registration
		user = form.save()
		login(self.request, user)
		return redirect('menu')


class LoginUser(DataMixin, LoginView):
	form_class = LoginUserForm
	template_name = 'inventory/login.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		mixin_context = self.get_user_context(title='Registration')

		return dict(list(context.items()) + list(mixin_context.items()))
	
	def get_success_url(self) -> str:	# "redirect" in LoginView
		return reverse_lazy('menu')


def LogoutUser(request):
	logout(request)
	return redirect('login')

#Exceptions
def pageNotFound(request, exception):
	return HttpResponseNotFound('<h1>ERROR 404</h1><br><p>Page Not Found</p>')