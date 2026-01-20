from rest_framework.viewsets import ModelViewSet
from .models import UsuarioModel
from management.models import EmpresaModel, RolModel
from .serializers import UsuarioSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action


class UsuarioViewSet(ModelViewSet):
    queryset = UsuarioModel.objects.select_related('empresa', 'rol').all()
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]
