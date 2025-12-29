from django.contrib import admin
from .models import UsuarioModel

# Register your models here.
@admin.register(UsuarioModel)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "tipo_documento", "numero_documento", "empresa", "activo")
    search_fields = ("nombre","apellido","numero_documento")