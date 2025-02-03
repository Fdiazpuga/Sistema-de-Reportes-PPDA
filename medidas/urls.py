from rest_framework.routers import DefaultRouter
from medidas.views import MedidaViewSet, ActividadViewSet

router = DefaultRouter()
router.register(r'medidas', MedidaViewSet, basename='medidas')
router.register(r'actividades', ActividadViewSet, basename='actividades')

urlpatterns = router.urls
