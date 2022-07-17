from django.urls import path
from .views import *


urlpatterns = [
	path('inventory', WarehouseView.as_view(), name='inventory'),
	path('ingredient/add', IngredientCreateView.as_view(), name='create_ingredient'),
	path('menu', MenuView.as_view(), name='menu'),
	path('purchases', PurchaseView.as_view(), name='purchase'),
	path('bookkeeping', FinanceView.as_view(), name='bookkeeping'),
	path('registration', RegisterUserView.as_view(), name='registration'),
	path('purchases/add', PurchaseCreateView.as_view(), name='create_purchase'),
]