from rest_framework import serializers
from ..models.empresa_model import EmpresaModel

class EmpresaSerializer(serializers.ModelSerializer):    
    class Meta:
        model = EmpresaModel
        fields = '__all__'
        
        def nombre_empresa(self, nombre_empresa):
            if not nombre_empresa:
                raise serializers.ValidationError("El nombre no puede estar vacio.")
            if len(nombre_empresa) <3:
                raise serializers.ValidationError("El nombre de la empresa debe ser mayor a 3 caracteres.")
            if nombre_empresa.isdigit():
                raise serializers.ValidationError("El nombre de la empresa no pueden ser solo numeros.")
            return nombre_empresa
        
        def nit(self,nit):
            if not nit:
                raise serializers.ValidationError("El NIT no puede estar vacio.")
            if len(nit) <3:
                raise serializers.ValidationError("El NIT debe ser mayor a 3 caracteres.")
            nit_registrado = EmpresaModel.objects.filter(nit=nit)
            if self.instance:
                nit_registrado = nit_registrado.exclude(pk=self.instance.pk)
                if nit_registrado.exists():
                    raise serializers.ValidationError("El NIT ya se encuentra registrado.")
            return nit