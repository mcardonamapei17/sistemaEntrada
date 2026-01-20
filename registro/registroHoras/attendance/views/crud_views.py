from rest_framework import viewsets, filters, pagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from ..models import RegistroEntrada
from ..serializers.crud_serializer import RegistroEntradaSerializer

class RegistroEntradaPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class RegistroEntradaViewSet(viewsets.ModelViewSet):
    queryset = RegistroEntrada.objects.select_related("usuario", "usuario__empresa", "sede").all()
    
    serializer_class = RegistroEntradaSerializer
    permission_classes = [AllowAny]
    pagination_class = RegistroEntradaPagination
    
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