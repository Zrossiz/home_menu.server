# Generated by Django 5.0.4 on 2024-05-24 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dish', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='image',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
