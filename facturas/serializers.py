from rest_framework import serializers
from .models import Inventario


class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = '__all__'


class SubirArchivoSerializer(serializers.Serializer):
    archivo = serializers.FileField()

    class Meta:
        fields = ['archivo']