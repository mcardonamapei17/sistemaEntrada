from rest_framework import serializers
from ..models.rol_model import RolModel

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolModel
        fields = '__all__'
        
        def validate_Rol(self,Rol):
            if not Rol:
                raise serializers.validationError("El campo Rol no puede estar vacio.")
            if len(Rol) < 3:
                raise serializers.ValidationError("El campo Rol debe tener al menos 3 caracteres.")
            if Rol.isdigit():
                raise serializers.ValidationError("El campo Rol no puede ser solo numeros.")
            return Rol