from django.db import models


class EmpresaModel(models.Model):
    nombre_empresa = models.CharField(max_length=150)
    direccion = models.CharField(max_length=255)
    TipoEmpresaChoices = [
        ("Interna","Interna"),
        ("Externa","Externa"),
    ]
    Tipo_empresa = models.CharField(max_length=10, choices=TipoEmpresaChoices)
    nit = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return f"{self.nombre_empresa} - {self.nit} - {self.Tipo_empresa}"
    
    