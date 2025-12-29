from django.contrib import admin
from management.models import EmpresaModel, SedeModel, RolModel

# Register your models here.
@admin.register(EmpresaModel)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ("nombre_empresa", "nit")
    search_fields = ("nombre_empresa", "nit")
    
@admin.register(SedeModel)
class SedeAdmin(admin.ModelAdmin):
    list_display = ("nombre_sede", "id_empresa")
    list_filter = ("id_empresa",)
    search_fields = ("nombre_sede",)
    
@admin.register(RolModel)
class RolAdmin(admin.ModelAdmin):
    list_display = ("Rol",)
    search_fields = ("Rol",)
    