from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from ..serializers.entrada_salida_serializer import (
    EntradaAsistenciaSerializer,
    SalidaAsistenciaSerializer
)


class EntradaAsistenciaView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = EntradaAsistenciaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        registro = serializer.save()

        return Response(
            {
                "mensaje": "Entrada registrada correctamente",
                "registro_id": registro.id,
                "fecha": registro.fecha,
                "hora_entrada": registro.hora_entrada,
            },
            status=status.HTTP_201_CREATED
        )


class SalidaAsistenciaView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = SalidaAsistenciaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        registro = serializer.save()

        return Response(
            {
                "mensaje": "Salida registrada correctamente",
                "registro_id": registro.id,
                "hora_salida": registro.hora_salida,
            },
            status=status.HTTP_200_OK
        )
