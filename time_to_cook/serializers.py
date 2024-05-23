from .models import TimeToCook
from rest_framework import serializers

class TimeToCookSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeToCook
        fields = "__all__"