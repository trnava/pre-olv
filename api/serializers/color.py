from rest_framework import serializers
from api.models.color import Color


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'
