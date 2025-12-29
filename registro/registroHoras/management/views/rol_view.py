from rest_framework import viewsets

from ..models.rol_model import RolModel
from ..serializers.rol_serializer import RolSerializer

class RolViewSet(viewsets.ModelViewSet):
    queryset = RolModel.objects.all();
    serializer_class = RolSerializer;
    