from rest_framework import viewsets,filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from ..models import RegistroEntrada
from ..serializers.crud_serializer import RegistroEntradaSerializer

class RegistroEntradaViewSet(viewsets.ModelViewSet):
    queryset = RegistroEntrada.objects.select_related("usuario","sede").all()
    
    serializer_class = RegistroEntradaSerializer
    permission_classes = [IsAuthenticated]
    
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    
    filterset_fields = [
        'usuario',
        'sede',
        'fecha',
        'hora_salida'
    ]
    
    ordering_fields = ['fecha','hora_entrada']
    ordering = ['-fecha','-hora_entrada']