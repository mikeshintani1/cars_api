from rest_framework import serializers
from .models import Car

# creating the serializer will allow for JSON/XML conversion
class CarSerializer(serializers.ModelSerializer):
    # a modelserializer will always use a meta subclass!
    class Meta:
        model = Car
        fields = ['id', 'make', 'model','year','price']