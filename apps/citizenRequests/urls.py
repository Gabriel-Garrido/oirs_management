from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (
    TipoSolicitudViewSet, ViaIngresoViewSet, AreaViewSet, SectorViewSet, GeneroViewSet, 
    EstadoRespuestaViewSet, TipoRespuestaViewSet, AtingenciaViewSet, SolicitudOIRSViewSet, 
    ArchivoSolicitudViewSet, SearchSolicitudOIRSView, initial_data, test_data
)

# Configurar el router para las rutas automáticas
router = DefaultRouter()
router.register(r'tipo-solicitud', TipoSolicitudViewSet)
router.register(r'via-ingreso', ViaIngresoViewSet)
router.register(r'area', AreaViewSet)
router.register(r'sector', SectorViewSet)
router.register(r'genero', GeneroViewSet)
router.register(r'estado-respuesta', EstadoRespuestaViewSet)
router.register(r'tipo-respuesta', TipoRespuestaViewSet)
router.register(r'atingencia', AtingenciaViewSet)
router.register(r'solicitudes', SolicitudOIRSViewSet)
router.register(r'archivos', ArchivoSolicitudViewSet)

# Definir las rutas URL
urlpatterns = [
    path('', include(router.urls)),  # Incluye las rutas generadas automáticamente por el router
    path('initial_data/', initial_data),  # Ruta para cargar los datos iniciales
    path('test_data/', test_data),  # Ruta para cargar los datos de prueba
    path('search_solicitudes/', SearchSolicitudOIRSView.as_view(), name='search_solicitudes'),  # Ruta para la búsqueda
]
