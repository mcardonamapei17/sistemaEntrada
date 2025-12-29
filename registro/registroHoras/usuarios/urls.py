from .views import UsuarioViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"usuarios", UsuarioViewSet, basename="usuarios")

urlpatterns = router.urls
