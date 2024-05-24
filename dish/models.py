from django.db import models
from category.models import Category
from time_to_cook.models import TimeToCook

# Create your models here.
class Dish(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    time_to_cook_id = models.ForeignKey(TimeToCook, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    image = models.CharField(blank=True, max_length=300)
    description = models.TextField()
    recipe = models.TextField()
    price = models.CharField(max_length=200)
    cooking_quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'dish'