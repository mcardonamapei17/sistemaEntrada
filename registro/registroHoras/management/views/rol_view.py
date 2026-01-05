from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from ..models.rol_model import RolModel
from ..serializers.rol_serializer import RolSerializer

class RolViewSet(viewsets.ModelViewSet):
    queryset = RolModel.objects.all();
    serializer_class = RolSerializer;
    permission_classes = [AllowAny]
    