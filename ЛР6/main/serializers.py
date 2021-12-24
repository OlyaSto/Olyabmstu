from .models import Rases
from rest_framework import serializers


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Rases
        # Поля, которые мы сериализуем
        fields = ["id","name", "discription"]