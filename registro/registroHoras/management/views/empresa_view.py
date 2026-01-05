from rest_framework.viewsets import ModelViewSet
from ..models.empresa_model import EmpresaModel
from ..serializers.empresa_serializer import EmpresaSerializer
from rest_framework.permissions import AllowAny

class EmpresaViewSet(ModelViewSet):
    queryset = EmpresaModel.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [AllowAny]
