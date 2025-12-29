from django.urls import path, include
from rest_framework.routers import DefaultRouter

from attendance.views.crud_views import RegistroEntradaViewSet
from attendance.views.entrada_salida_views import (
    EntradaAsistenciaView,
    SalidaAsistenciaView,
)
from attendance.views.buscar_documento_view import BuscarDocumentoView

router = DefaultRouter()
router.register(
    r"registro-entrada",
    RegistroEntradaViewSet,
    basename="registro-entrada"
)

urlpatterns = [
    # CRUD completo
    path("", include(router.urls)),

    # acciones específicas
    path("entrada/", EntradaAsistenciaView.as_view(), name="entrada-asistencia"),
    path("salida/", SalidaAsistenciaView.as_view(), name="salida-asistencia"),
    path(
        "buscar-documento/",
        BuscarDocumentoView.as_view(),
        name="buscar-documento"
    ),
]
