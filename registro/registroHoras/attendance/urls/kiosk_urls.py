from django.urls import path
from attendance.views.buscar_documento_view import BuscarDocumentoView

urlpatterns = [
    path(
        "buscar-documento/",
        BuscarDocumentoView.as_view(),
        name="buscar-documento"
    ),
]
