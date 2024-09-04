from rest_framework import viewsets, status, permissions
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from django.core.management import call_command

from .models import TipoSolicitud, ViaIngreso, Area, Sector, Genero, EstadoRespuesta, TipoRespuesta, Atingencia, SolicitudOIRS, ArchivoSolicitud
from .serializers import (
    TipoSolicitudSerializer, ViaIngresoSerializer, AreaSerializer, SectorSerializer, GeneroSerializer, 
    EstadoRespuestaSerializer, TipoRespuestaSerializer, AtingenciaSerializer, SolicitudOIRSSerializer, 
    ArchivoSolicitudSerializer
)
from .pagination import SmallSetPagination, MediumSetPagination, LargeSetPagination

# ViewSets para los modelos básicos
#ViewSet: Es una clase que agrupa todas las operaciones CRUD para un modelo en particular. Por ejemplo, TipoSolicitudViewSet maneja todas las operaciones para el modelo TipoSolicitud

class TipoSolicitudViewSet(viewsets.ModelViewSet):
    #queryset: Define qué registros vamos a mostrar en nuestra API. En este caso, estamos diciendo que se muestren todos los registros de TipoSolicitud.
    queryset = TipoSolicitud.objects.all()
    #serializer_class: Especifica qué serializador vamos a usar para convertir los datos de los modelos a JSON y viceversa.
    serializer_class = TipoSolicitudSerializer

class ViaIngresoViewSet(viewsets.ModelViewSet):
    queryset = ViaIngreso.objects.all()
    serializer_class = ViaIngresoSerializer

class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class SectorViewSet(viewsets.ModelViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class EstadoRespuestaViewSet(viewsets.ModelViewSet):
    queryset = EstadoRespuesta.objects.all()
    serializer_class = EstadoRespuestaSerializer

class TipoRespuestaViewSet(viewsets.ModelViewSet):
    queryset = TipoRespuesta.objects.all()
    serializer_class = TipoRespuestaSerializer

class AtingenciaViewSet(viewsets.ModelViewSet):
    queryset = Atingencia.objects.all()
    serializer_class = AtingenciaSerializer

# ViewSet para la SolicitudOIRS con paginación
class SolicitudOIRSViewSet(viewsets.ModelViewSet):
    queryset = SolicitudOIRS.objects.all()
    serializer_class = SolicitudOIRSSerializer
    pagination_class = LargeSetPagination  # Aquí especificas la clase de paginación

    def create(self, request, *args, **kwargs):
        #request.data: Aquí obtenemos los datos que el usuario envió para crear una nueva solicitud.
        data = request.data
        data['creado_por'] = request.user.id
        serializer = self.get_serializer(data=data)
        #serializer.is_valid(): Verificamos si los datos enviados son válidos según las reglas definidas en el serializer.
        serializer.is_valid(raise_exception=True)
        #perform_create(): Guarda la nueva solicitud en la base de datos.
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        #get_object(): Obtiene la solicitud específica que queremos actualizar.
        instance = self.get_object()
        data = request.data
        data['ultima_modificacion'] = instance.ultima_modificacion  # Mantener la fecha de modificación automática
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        #perform_update(): Actualiza la solicitud en la base de datos.
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        return Response(serializer.data)

    #action: Nos permite crear acciones personalizadas dentro de un ViewSet (como la función upload_file más adelante).
    @action(detail=True, methods=['post'], url_path='upload-file', url_name='upload_file')
    def upload_file(self, request, pk=None):
        solicitud = self.get_object()
        archivo = request.FILES.get('archivo')
        descripcion = request.data.get('descripcion')

        if archivo and descripcion:
            archivo_solicitud = ArchivoSolicitud.objects.create(
                solicitud=solicitud,
                archivo=archivo,
                descripcion=descripcion
            )
            archivo_solicitud.save()
            serializer = ArchivoSolicitudSerializer(archivo_solicitud)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"detail": "Archivo y descripción son requeridos."}, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(creado_por=self.request.user)

    def perform_update(self, serializer):
        serializer.save(ultima_modificacion=self.request.user)

# ViewSet para los Archivos de Solicitud

class ArchivoSolicitudViewSet(viewsets.ModelViewSet):
    queryset = ArchivoSolicitud.objects.all()
    serializer_class = ArchivoSolicitudSerializer

    def get_queryset(self):
        solicitud_id = self.kwargs.get('solicitud_pk')
        return self.queryset.filter(solicitud__id=solicitud_id)

# Vista para cargar datos iniciales desde un fixture.
#api_view: Es un decorador que se utiliza para crear vistas basadas en funciones. Aquí se usa para las vistas initial_data y test_data.
#call_command: Nos permite ejecutar comandos de Django desde nuestro código, como cargar datos iniciales desde un archivo JSON.
@api_view(['GET'])
def initial_data(request):
    call_command('loaddata', 'initial_data.json')
    return Response({"detail": "Initial data uploaded successfully"})

@api_view(['GET'])
def test_data(request):
    call_command('loaddata', 'test_data.json')
    return Response({"detail": "Test data uploaded successfully"})

class SearchSolicitudOIRSView(APIView):
    permission_classes = (permissions.AllowAny, )  
    # Permite el acceso a cualquier usuario

    def get(self, request, format=None):
        # Aquí obtenemos el término de búsqueda desde los parámetros de la URL (ejemplo: ?s=consulta).
        search_term = request.query_params.get('s', None)

        # Comprobar si hay un término de búsqueda
        if search_term:
            # Filtrar las solicitudes que coincidan con el término en ciertos campos
            #Q: Es una herramienta de Django que nos permite realizar consultas complejas. En este caso, estamos buscando coincidencias en varios campos del modelo SolicitudOIRS:
            matches = SolicitudOIRS.objects.filter(
                Q(folio__icontains=search_term) |  # Busca en el campo 'folio'
                Q(nombre_usuario__icontains=search_term) |  # Busca en el nombre del usuario
                Q(funcionario_aludido__icontains=search_term) |  # Busca en el funcionario aludido
                Q(texto_solicitud__icontains=search_term) |  # Busca en el texto de la solicitud
                Q(tipo_solicitud__nombre__icontains=search_term)  # Busca en el nombre del tipo de solicitud
            )
        else:
            matches = SolicitudOIRS.objects.none()  # Si no hay término de búsqueda, no devolver nada

        # Paginación
        paginator = LargeSetPagination()
        results = paginator.paginate_queryset(matches, request)

        # Serializar los resultados
        serializer = SolicitudOIRSSerializer(results, many=True)

        # Devolver la respuesta paginada
        return paginator.get_paginated_response({'filtered_solicitudes': serializer.data})
