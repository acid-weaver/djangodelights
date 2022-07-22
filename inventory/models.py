from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Ingredient(models.Model):
	title = models.CharField(max_length=63, unique=True)
	quantity = models.DecimalField(max_digits=12, decimal_places=6, default=0)
	class PossibleUnits(models.TextChoices):
		GRAM = 'g.', _('grams')
		KILO = 'kg.', _('kilos')
		LITER = 'L.', _('liters')
		MLITER = 'ml.', _('milliliters')
		AMOUNT = 'num', _('amount')
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
	menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='recipe')
	ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
	require = models.DecimalField(max_digits=12, decimal_places=6, default=1)
	def __str__(self):
		return 'For {}: {} {} {}'.format(self.menu_item.title, str(self.require), self.ingredient.unit, self.ingredient.title)


class Purchase(models.Model):
	menu_items = models.JSONField(null=True)
	client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
	time_create = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return 'Purchase #{}'.format(self.pk)

	@property
	def total_price(self):
		sum = 0
		for item in dict(self.menu_items).items():
			sum += MenuItem.objects.get(title=item[0]).price * item[1]
		return sum

	@property
	def total_expenses(self):
		sum = 0
		for item in self.menu_items.items():
			for i in MenuItem.objects.get(title=item[0]).recipe.all():	# used related_name for Recipe Requirements
				sum += i.ingredient.price * i.require * item[1]
		return sum

	@property
	def modify_inventory(self):
		for item in self.menu_items.items():
			for i in MenuItem.objects.get(title=item[0]).recipe.all():
				i.ingredient.quantity -= i.require * item[1]
				i.ingredient.save()
		return True