from rest_framework.routers import DefaultRouter
from .views import EmpresaViewSet, RolViewSet, SedeViewSet

router = DefaultRouter()
router.register(r"empresas",EmpresaViewSet)
router.register(r"sedes",SedeViewSet)
router.register(r"roles",RolViewSet)

urlpatterns = router.urls
