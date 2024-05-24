from django.db import models

class TimeToCook(models.Model):
    time = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.time) + ' мин.'

    class Meta:
        db_table = 'time_to_cook'