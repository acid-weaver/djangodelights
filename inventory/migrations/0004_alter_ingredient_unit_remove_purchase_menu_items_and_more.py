# Generated by Django 4.0.4 on 2022-07-16 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_ingredient_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(blank=True, choices=[('g.', 'grams'), ('kg.', 'kilos'), ('L.', 'liters'), ('ml.', 'milliliters'), ('', 'amount')], default='', max_length=3),
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='menu_items',
        ),
        migrations.AddField(
            model_name='purchase',
            name='menu_items',
            field=models.JSONField(null=True),
        ),
    ]