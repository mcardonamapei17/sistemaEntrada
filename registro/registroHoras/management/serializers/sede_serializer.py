from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from ..models.sede_model import SedeModel
from ..models.empresa_model import EmpresaModel


class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SedeModel
        fields = '__all__'

    def validate(self, attrs):
        # Validate possible name field (try common names)
        nombre = attrs.get('nombre_sede') or attrs.get('nombre')
        if nombre is not None:
            if not nombre:
                raise ValidationError("El campo Nombre no puede estar vacio.")
            if len(nombre) < 3:
                raise ValidationError("El campo nombre no puede ser menor a 3 caracteres.")
            if nombre.isdigit():
                raise ValidationError("El campo nombre no puede contener solo numeros.")

        # Validate empresa/id_empresa if provided
        id_empresa = attrs.get('id_empresa') or attrs.get('empresa')
        if id_empresa is not None:
            try:
                if hasattr(id_empresa, 'id'):
                    EmpresaModel.objects.get(id=id_empresa.id)
                else:
                    EmpresaModel.objects.get(id=id_empresa)
            except EmpresaModel.DoesNotExist:
                raise ValidationError("La empresa proporcionada no existe.")

        return attrs
                