# Generated by Django 5.0.4 on 2024-05-24 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dish', '0003_alter_dish_cooking_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dish',
            old_name='cateogory_id',
            new_name='category_id',
        ),
    ]