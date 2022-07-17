from django.urls import path
from .views import *


urlpatterns = [
	path('inventory', WarehouseView.as_view(), name='inventory'),
	path('inventory/add', IngredientCreateView.as_view(), name='create_ingredient'),
	path('inventory/<pk>', IngredientUpdateView.as_view(), name='update_ingredient'),
	path('inventory/<pk>/delete', IngredientDeleteView.as_view(), name='delete_ingredient'),
	path('menu', MenuView.as_view(), name='menu'),
	path('purchases', PurchaseView.as_view(), name='purchase'),
	path('purchases/add', PurchaseCreateView.as_view(), name='create_purchase'),
	path('purchases/<pk>/delete', PurchaseDeleteView.as_view(), name='delete_purchase'),
	path('bookkeeping', FinanceView.as_view(), name='bookkeeping'),
	path('registration', RegisterUser.as_view(), name='registration'),
	path('login', LoginUser.as_view(), name='login'),
	path('logout', LogoutUser, name='logout'),
]