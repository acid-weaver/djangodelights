# Generated by Django 4.0.4 on 2022-07-16 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_ingredient_unit_remove_purchase_menu_items_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
    ]