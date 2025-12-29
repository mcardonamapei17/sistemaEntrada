from rest_framework.viewsets import ModelViewSet
from .models import UsuarioModel
from .serializers import UsuarioSerializer


class UsuarioViewSet(ModelViewSet):
    queryset = UsuarioModel.objects.select_related('empresa').all()
    serializer_class = UsuarioSerializer
