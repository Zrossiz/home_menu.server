# Generated by Django 5.0.6 on 2024-05-24 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('time_to_cook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetocook',
            name='time',
            field=models.IntegerField(),
        ),
    ]
