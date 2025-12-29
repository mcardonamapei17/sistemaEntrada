from rest_framework import serializers
from ..models.sede_model import SedeModel
from ..models.empresa_model import EmpresaModel

class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SedeModel
        fields = '__all__'
        
        def validate_Sede(self,nombre_sede):
            if not nombre_sede:
                raise serializers.ValidationError("El campo Nombre no puede estar vacio.")
            if len(nombre_sede) <3: 
                raise serializers.ValidationError("El campo nombre no puede ser menor a 3 caracteres.")
            if nombre_sede.isdigit():
                raise serializers.ValidationError("El campo nombre no pede contener solo numeros.")
            
        def validate_id_empresa(self,id_empresa):
            if not id_empresa:
                raise serializers.ValidationError("El campo id empresa no puede estar vacio.")
            
            try:
                EmpresaModel.objects.get(id=id_empresa.id)
            except EmpresaModel.DoesNotExist:
                raise serializers.validationError("La empresa proporcionada no existe.")
            return id_empresa
                