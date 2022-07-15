from tkinter import CASCADE
from django.db import models
from django.conf import settings

# Create your models here.
class Ingredient(models.Model):
	title = models.CharField(max_length=63, unique=True)
	quantity = models.PositiveIntegerField(default=0)
	price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	def __str__(self):
		return self.title

class MenuItem(models.Model):
	title = models.CharField(max_length=255, unique=True)
	price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	def __str__(self):
		return self.title

class RecipeRequirements(models.Model):
	menu_item = models.OneToOneField(MenuItem, on_delete=models.CASCADE)
	ingredients = models.ManyToManyField(Ingredient)
	require = models.JSONField()

class Purchase(models.Model):
	menu_items = models.ManyToManyField(MenuItem)
	client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)