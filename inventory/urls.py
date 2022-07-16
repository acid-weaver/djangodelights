from django.urls import path
from .views import *


urlpatterns = [
	path('inventory', WarehouseView.as_view(), name='inventory'),
]