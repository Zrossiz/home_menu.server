# Generated by Django 5.0.6 on 2024-05-23 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
