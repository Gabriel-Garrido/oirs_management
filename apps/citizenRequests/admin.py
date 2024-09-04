from django.contrib import admin
from .models import (
    TipoSolicitud, ViaIngreso, Area, Sector, Genero, EstadoRespuesta, TipoRespuesta, 
    Atingencia, SolicitudOIRS, ArchivoSolicitud
)

# Registro de los modelos básicos en el admin

@admin.register(TipoSolicitud)
class TipoSolicitudAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['nombre']

@admin.register(ViaIngreso)
class ViaIngresoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['nombre']

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['nombre']

@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['nombre']

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['nombre']

@admin.register(EstadoRespuesta)
class EstadoRespuestaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['nombre']

@admin.register(TipoRespuesta)
class TipoRespuestaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['nombre']

@admin.register(Atingencia)
class AtingenciaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['nombre']

# Configuración del admin para SolicitudOIRS

class ArchivoSolicitudInline(admin.TabularInline):
    model = ArchivoSolicitud
    extra = 1
    readonly_fields = ['fecha_carga']

@admin.register(SolicitudOIRS)
class SolicitudOIRSAdmin(admin.ModelAdmin):
    list_display = ['folio', 'tipo_solicitud', 'nombre_usuario', 'fecha_recepcion', 'estado_respuesta']
    list_filter = ['tipo_solicitud', 'via_ingreso', 'area', 'sector', 'genero', 'estado_respuesta']
    search_fields = ['folio', 'nombre_usuario', 'rut_usuario', 'funcionario_aludido', 'tema']
    inlines = [ArchivoSolicitudInline]
    readonly_fields = ['creado_por', 'fecha_creacion', 'ultima_modificacion']
    fieldsets = (
        (None, {
            'fields': ('tipo_solicitud', 'folio', 'via_ingreso', 'tema', 'area', 'sector', 'genero', 
                       'fecha_recepcion', 'fecha_maxima_respuesta', 'fecha_respuesta_entregada', 
                       'fecha_envio_funcionario', 'fecha_recepcion_descargo', 'tipo_respuesta', 
                       'estado_respuesta', 'texto_solicitud', 'nombre_usuario', 'rut_usuario', 
                       'funcionario_aludido', 'atingencia', 'creado_por', 'fecha_creacion', 
                       'ultima_modificacion')
        }),
    )

# Registro del modelo ArchivoSolicitud en el admin

@admin.register(ArchivoSolicitud)
class ArchivoSolicitudAdmin(admin.ModelAdmin):
    list_display = ['solicitud', 'descripcion', 'fecha_carga']
    search_fields = ['solicitud__folio', 'descripcion']
    readonly_fields = ['fecha_carga']
