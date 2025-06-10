from rest_framework import serializers
from .models import Poruka

class PorukaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poruka
        fields = ['tekst']