from rest_framework.viewsets import ModelViewSet
from ..models.sede_model import SedeModel
from ..serializers.sede_serializer import SedeSerializer

class SedeViewSet(ModelViewSet):
    queryset = SedeModel.objects.all()
    serializer_class = SedeSerializer
