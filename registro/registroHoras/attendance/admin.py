from django.contrib import admin
from .models import RegistroEntrada
from django.utils import timezone


@admin.register(RegistroEntrada)
class RegistroAsistenciaAdmin(admin.ModelAdmin):
    list_display = (
        'usuario',
        'sede',
        'fecha',
        'hora_entrada',
        'hora_salida',
        'estado',
        'placa_vehiculo',
        'EPP_entregados',
        'Informacion_recibida',
    )

    list_filter = (
        'sede',
        'fecha',
        'hora_salida',
    )

    search_fields = (
        'usuario__nombre',
        'usuario__apellido',
        'usuario__numero_documento',
    )

    ordering = ('-fecha', '-hora_entrada')

    autocomplete_fields = ['usuario', 'sede']

    readonly_fields = ('fecha', 'hora_entrada')

    fieldsets = (
        ('Información del Usuario', {
            'fields': ('usuario', 'sede','placa_vehiculo','EPP_entregados','Informacion_recibida')
        }),
        ('Registro de Asistencia', {
            'fields': ('fecha', 'hora_entrada', 'hora_salida')
        }),
    )
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.fecha = timezone.localdate()
            obj.hora_entrada = timezone.now()
        super().save_model(request, obj, form, change)

    def estado(self, obj):
        return "🟢 Abierto" if obj.hora_salida is None else "🔴 Cerrado"

    estado.short_description = "Estado"
