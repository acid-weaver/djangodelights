from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Ingredient(models.Model):
	title = models.CharField(max_length=63, unique=True)
	quantity = models.PositiveIntegerField(default=0)
	class PossibleUnits(models.TextChoices):
		GRAM = 'g.', _('grams')
		KILO = 'kg.', _('kilos')
		LITER = 'L.', _('liters')
		MLITER = 'ml.', _('milliliters')
		AMOUNT = '', _('amount')
	unit = models.CharField(max_length=3, choices=PossibleUnits.choices, default=PossibleUnits.AMOUNT)
	price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	def __str__(self):
		return self.title

class MenuItem(models.Model):
	title = models.CharField(max_length=255, unique=True)
	price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	def __str__(self):
		return self.title

class RecipeRequirement(models.Model):
	menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
	ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
	require = models.PositiveIntegerField(default=1)
	def __str__(self):
		return '{} {} {}'.format(str(self.require), self.ingredient.unit, self.ingredient.title)

class Purchase(models.Model):
	menu_items = models.ManyToManyField(MenuItem)
	client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
	def __str__(self):
		return 'Purchase #{}'.format(self.pk)