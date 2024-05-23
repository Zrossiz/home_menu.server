from django.db import models
from category.models import Category
from time_to_cook.models import TimeToCook

# Create your models here.
class Dish(models.Model):
    cateogory_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    time_to_cook_id = models.ForeignKey(TimeToCook, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=300)
    description = models.TextField()
    recipe = models.TextField()
    price = models.CharField(max_length=200)
    cooking_quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'dish'