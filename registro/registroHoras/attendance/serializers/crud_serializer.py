from rest_framework import serializers
from ..models import RegistroEntrada

class RegistroEntradaSerializer(serializers.ModelSerializer):
    usuario_nombre = serializers.SerializerMethodField()
    sede_nombre = serializers.SerializerMethodField()

    def get_usuario_nombre(self, obj):
        return f"{obj.usuario.nombre} {obj.usuario.apellido}"

    def get_sede_nombre(self, obj):
        return obj.sede.nombre_sede
    
    class Meta:
        model = RegistroEntrada
        fields = [
            'id',
            'usuario',
            'usuario_nombre',
            'sede',
            'sede_nombre',
            'fecha',
            'hora_entrada',
            'hora_salida',
            'placa_vehiculo',
            'EPP_entregados',
            'Informacion_recibida',
        ]
        read_only_fields = ['id']
        
    def validate(self, data):
        usuario = data.get('usuario')
        fecha = data.get("fecha")
            
        if self.instance is None:
            existe = RegistroEntrada.objects.filter(
                usuario=usuario,
                fecha=fecha,
                hora_salida__isnull=True
            ).exists()
                
            if existe:
                raise serializers.ValidationError(f"El usuario ya tiene un registro de entrada abrierto en la fecha {self.fecha}")
                
        return data
