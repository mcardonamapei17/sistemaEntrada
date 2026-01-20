#imports de librerias
from django.db import models    
from django.db.models import Q
from decimal import Decimal

#imports de otros modelos
from usuarios.models import UsuarioModel
from management.models.sede_model import SedeModel
from vehiculos.models import VehiculoModel

class RegistroEntrada(models.Model):
    
    #datos de seguimiento, usuario, sede, vehiculo
    usuario = models.ForeignKey(UsuarioModel, on_delete=models.CASCADE, null=True , blank=True)
    sede = models.ForeignKey(SedeModel, on_delete=models.PROTECT)
    vehiculo = models.ForeignKey(VehiculoModel, on_delete=models.SET_NULL, null=True, blank=True)
    
    #Logica cargue y descargue
    es_caragueDescargue = models.BooleanField(default=False)
    
    #datos extas del conductor por si es cargue y descargue
    nombre_conductor_externo = models.CharField(max_length=255, null=True, blank=True)
    documento_conductor_externo = models.CharField(max_length=50, null=True, blank=True)
    
    #pesaje del vehiculo al llegar y al salir
    peso_inicial = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    peso_final = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    
    #Tiempos, fechas y control
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
                condition = Q(hora_salida__isnull = True, usuario__isnull = True),
                name = "una_entrada_abierta_por_usuario_por_dia"
            ),
            models.UniqueConstraint(
                fields = ['vehiculo','fecha'],
                condition= Q(hora_salida__isnull = True, vehiculo__isnull = True),
                name = "un_vehiculo_entrada_abierta_por_dia"
            )
        ]
        indexes = [
            models.Index(fields=['usuario','fecha']),
            models.Index(fields=["vehiculo","fecha"]),
            models.Index(fields=["hora_salida"]),
        ]
        
    @property
    def peso_neto(self):
        if self.peso_inicial is not None and self.peso_final is not None:
            return abs(self.peso_final - self.peso_inicial)
        return Decimal('0.000')
        
    def __str__(self):
        return f"{self.usuario} - {self.fecha} - {self.hora_entrada} - {self.hora_salida}"