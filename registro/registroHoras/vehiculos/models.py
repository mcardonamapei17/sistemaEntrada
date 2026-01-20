from django.db import models
from management.models.empresa_model import EmpresaModel

# Create your models here.
class VehiculoModel(models.Model):
    TIPO_VEHICULO_CHOICES = [
        ("PESADO","Carga / Pesado"),
        ("LIVIANO", "Particular / Liviano"),
        ("MOTOCICLETA", "Motocicleta"),
    ]
    
    placa = models.CharField(max_length=15, unique=True)
    
    empresa = models.ForeignKey(EmpresaModel, on_delete=models.PROTECT, null=True, blank=True)
    tipo_vehiculo = models.CharField(max_length=30,choices=TIPO_VEHICULO_CHOICES, default="LIVIANO")
    
    soat_vigente = models.BooleanField()
    tecnomecanica_vigente = models.BooleanField()
    
    def __str__(self):
        return f"{self.placa} - {self.tipo_vehiculo} - {self.empresa.nombre_empresa}"