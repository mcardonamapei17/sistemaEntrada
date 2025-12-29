from django.db import models    
from django.db.models import Q
from usuarios.models import UsuarioModel
from management.models.sede_model import SedeModel

class RegistroEntrada(models.Model):
    usuario = models.ForeignKey(UsuarioModel, on_delete=models.CASCADE)
    sede = models.ForeignKey(SedeModel, on_delete=models.PROTECT)
    
    fecha = models.DateField()
    hora_entrada = models.DateTimeField()
    hora_salida = models.DateTimeField(null= True, blank=True)
    placa_vehiculo = models.CharField(max_length=30, null=True, blank=True)
    EPP_entregados = models.BooleanField(default=False)
    Informacion_recibida = models.BooleanField(default=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ['usuario','fecha'],
                condition = Q(hora_salida__isnull = True),
                name = "una_entrada_abierta_por_usuario_por_dia"
            )
        ]
        indexes = [
            models.Index(fields=['usuario','fecha']),
            models.Index(fields=["hora_salida"]),
        ]
        
    def __str__(self):
        return f"{self.usuario} - {self.fecha} - {self.hora_entrada} - {self.hora_salida}"