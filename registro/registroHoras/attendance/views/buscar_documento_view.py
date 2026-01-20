from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from usuarios.models import UsuarioModel
from attendance.models import RegistroEntrada


class BuscarDocumentoView(APIView):
    """
    Endpoint de kiosko:
    Busca un usuario por documento y devuelve su estado actual
    """

    authentication_classes = []   # luego aquí irá API Key
    permission_classes = []

    def get(self, request):
        documento = request.query_params.get("documento")

        if not documento:
            return Response(
                {"detail": "El documento es obligatorio"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            usuario = UsuarioModel.objects.select_related(
                "empresa"
            ).get(numero_documento=documento)

        except UsuarioModel.DoesNotExist:
            return Response(
                {
                    "existe": False,
                    "requiere_registro": True
                },
                status=status.HTTP_200_OK
            )

        # Buscar entrada abierta
        registro_abierto = (
            RegistroEntrada.objects
            .select_related("sede")
            .filter(usuario=usuario, hora_salida__isnull=True)
            .order_by("-hora_entrada")
            .first()
        )

        # Buscar última salida registrada
        ultima_salida = (
            RegistroEntrada.objects
            .select_related("sede")
            .filter(usuario=usuario, hora_salida__isnull=False)
            .order_by("-hora_salida")
            .first()
        )

        data = {
            "existe": True,
            "tipo": usuario.rol.id if hasattr(usuario, "rol") else usuario.tipo,
            "usuario": {
                "id": usuario.id,
                "nombre": usuario.nombre,
                "apellido": usuario.apellido,
                "documento": usuario.numero_documento,
            },
            "entrada_abierta": bool(registro_abierto),
        }

        # Empresa
        if usuario.empresa:
            data["empresa"] = {
                "id": usuario.empresa.id,
                "nombre": usuario.empresa.nombre_empresa,
                "nit": usuario.empresa.nit,
            }
        else:
            data["empresa"] = None
            data["empresa_requerida"] = True

        # Registro abierto (para salida)
        if registro_abierto:
            data["registro"] = {
                "id": registro_abierto.id,
                "fecha": registro_abierto.fecha,
                "hora_entrada": registro_abierto.hora_entrada,
                "sede": {
                    "id": registro_abierto.sede.id,
                    "nombre": registro_abierto.sede.nombre_sede,
                }
            }

        # Última salida registrada
        if ultima_salida:
            data["ultima_salida"] = {
                "id": ultima_salida.id,
                "fecha": ultima_salida.fecha,
                "hora_entrada": ultima_salida.hora_entrada,
                "hora_salida": ultima_salida.hora_salida,
                "sede": {
                    "id": ultima_salida.sede.id,
                    "nombre": ultima_salida.sede.nombre_sede,
                }
            }

        return Response(data, status=status.HTTP_200_OK)
