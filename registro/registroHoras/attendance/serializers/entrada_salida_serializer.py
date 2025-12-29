from rest_framework import serializers
from django.utils import timezone
from attendance.models import RegistroEntrada
from usuarios.models import UsuarioModel
from management.models.sede_model import SedeModel


class EntradaAsistenciaSerializer(serializers.Serializer):
    usuario_id = serializers.IntegerField()
    sede_id = serializers.IntegerField()

    placa_vehiculo = serializers.CharField(
        required=False, allow_blank=True, allow_null=True
    )
    EPP_entregados = serializers.BooleanField(default=False)
    Informacion_recibida = serializers.BooleanField(default=True)

    def validate(self, data):
        hoy = timezone.localdate()

        if RegistroEntrada.objects.filter(
            usuario_id=data['usuario_id'],
            fecha=hoy,
            hora_salida__isnull=True
        ).exists():
            raise serializers.ValidationError(
                "El usuario ya tiene una entrada abierta hoy."
            )

        return data

    def create(self, validated_data):
        usuario = UsuarioModel.objects.get(id=validated_data['usuario_id'])
        sede = SedeModel.objects.get(id=validated_data['sede_id'])

        return RegistroEntrada.objects.create(
            usuario=usuario,
            sede=sede,
            fecha=timezone.localdate(),
            hora_entrada=timezone.now(),
            placa_vehiculo=validated_data.get('placa_vehiculo'),
            EPP_entregados=validated_data.get('EPP_entregados', False),
            Informacion_recibida=validated_data.get('Informacion_recibida', True),
        )


class SalidaAsistenciaSerializer(serializers.Serializer):
    usuario_id = serializers.IntegerField()

    def validate(self, data):
        hoy = timezone.localdate()

        if not RegistroEntrada.objects.filter(
            usuario_id=data['usuario_id'],
            fecha=hoy,
            hora_salida__isnull=True
        ).exists():
            raise serializers.ValidationError(
                "No existe una entrada abierta para hoy."
            )

        return data

    def save(self):
        hoy = timezone.localdate()

        registro = RegistroEntrada.objects.get(
            usuario_id=self.validated_data['usuario_id'],
            fecha=hoy,
            hora_salida__isnull=True
        )

        registro.hora_salida = timezone.now()
        registro.save()
        return registro
