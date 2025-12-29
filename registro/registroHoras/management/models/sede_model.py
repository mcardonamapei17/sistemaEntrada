from django.db import models
from .empresa_model import EmpresaModel

class SedeModel(models.Model):
    nombre_sede = models.CharField(max_length=150)
    direccion = models.CharField(max_length=255)
    id_empresa = models.ForeignKey(EmpresaModel, on_delete=models.CASCADE, related_name="sedes")
    
    def __str__(self):
        return f"{self.nombre_sede} - {self.direccion} - {self.id_empresa.nombre_empresa}"