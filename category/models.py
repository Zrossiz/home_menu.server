from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=300, blank=False, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'category'