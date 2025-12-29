from rest_framework import serializers
from .models import UsuarioModel


class UsuarioSerializer(serializers.ModelSerializer):
    empresa_nombre = serializers.CharField(
        source='empresa.nombre',
        read_only=True
    )

    class Meta:
        model = UsuarioModel
        fields = [
            'id',
            'nombre',
            'apellido',
            'tipo_documento',
            'numero_documento',
            'empresa',
            'empresa_nombre',
            'activo',
            'fecha_creacion',
        ]
        read_only_fields = ('id', 'fecha_creacion')
