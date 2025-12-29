from django.db import models
from management.models.empresa_model import EmpresaModel
from management.models.rol_model import RolModel

# Create your models here.
class UsuarioModel(models.Model):
    TipoDocumento_choices = [
        ("CC","Cedula de ciudadania"),
        ("CE","Cedula de extranjeria"),
        ("PA","Pasaporte"),
        ("NIT","Numero de indentificacion tributaria"),
    ]
    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    tipo_documento = models.CharField(max_length=100,choices=TipoDocumento_choices)
    numero_documento = models.CharField(max_length=50, unique=True)
    
    empresa = models.ForeignKey(EmpresaModel, on_delete=models.PROTECT)
    rol = models.ForeignKey(RolModel, on_delete=models.PROTECT)
    
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    ARL = models.CharField(max_length=100, null=True, blank=True)
    EPS = models.CharField(max_length=100, null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.numero_documento}"