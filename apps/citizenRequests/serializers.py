from rest_framework import serializers
from .models import TipoSolicitud, ViaIngreso, Area, Sector, Genero, EstadoRespuesta, TipoRespuesta, Atingencia, SolicitudOIRS, ArchivoSolicitud

class TipoSolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSolicitud
        fields = ['id', 'nombre']

class ViaIngresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViaIngreso
        fields = ['id', 'nombre']

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ['id', 'nombre']

class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = ['id', 'nombre']

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ['id', 'nombre']

class EstadoRespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoRespuesta
        fields = ['id', 'nombre']

class TipoRespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoRespuesta
        fields = ['id', 'nombre']

class AtingenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atingencia
        fields = ['id', 'nombre']

class ArchivoSolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchivoSolicitud
        fields = ['id', 'solicitud', 'archivo', 'descripcion', 'fecha_carga']
        read_only_fields = ['fecha_carga']

class SolicitudOIRSSerializer(serializers.ModelSerializer):
    archivos = ArchivoSolicitudSerializer(many=True, read_only=True)
    tipo_solicitud = TipoSolicitudSerializer()
    via_ingreso = ViaIngresoSerializer()
    area = AreaSerializer()
    sector = SectorSerializer()
    genero = GeneroSerializer()
    tipo_respuesta = TipoRespuestaSerializer()
    estado_respuesta = EstadoRespuestaSerializer()
    atingencia = AtingenciaSerializer()

    class Meta:
        model = SolicitudOIRS
        fields = [
            'id', 'tipo_solicitud', 'folio', 'via_ingreso', 'tema', 'area', 'sector', 
            'genero', 'fecha_recepcion', 'fecha_maxima_respuesta', 'fecha_respuesta_entregada',
            'fecha_envio_funcionario', 'fecha_recepcion_descargo', 'tipo_respuesta', 
            'estado_respuesta', 'texto_solicitud', 'nombre_usuario', 'rut_usuario', 
            'funcionario_aludido', 'atingencia', 'creado_por', 'fecha_creacion', 
            'ultima_modificacion', 'archivos'
        ]
        read_only_fields = ['creado_por', 'fecha_creacion', 'ultima_modificacion']
