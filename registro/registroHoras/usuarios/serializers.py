from rest_framework import serializers
from .models import UsuarioModel


class UsuarioSerializer(serializers.ModelSerializer):
    empresa_nombre = serializers.CharField(
        source='empresa.nombre_empresa',
        read_only=True
    )
    rol_nombre = serializers.CharField(
        source='rol.nombre',
        read_only=True,
        required=False
    )

    class Meta:
        model = UsuarioModel
        fields = [
            'id',
            'nombre',
            'apellido',
            'rol',
            'rol_nombre',
            'tipo_documento',
            'numero_documento',
            'empresa',
            'empresa_nombre',
            'ARL',
            'EPS',
            'activo',
            'fecha_creacion',
        ]
        read_only_fields = ('id', 'fecha_creacion')
