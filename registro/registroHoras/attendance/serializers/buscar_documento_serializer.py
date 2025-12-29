from rest_framework import serializers


class BuscarDocumentoResponseSerializer(serializers.Serializer):
    existe = serializers.BooleanField()
    tipo = serializers.CharField(required=False)

    usuario = serializers.DictField(required=False)
    empresa = serializers.DictField(required=False, allow_null=True)

    empresa_requerida = serializers.BooleanField(required=False)
    entrada_abierta = serializers.BooleanField(required=False)

    registro = serializers.DictField(required=False)
