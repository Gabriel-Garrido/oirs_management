from django.db import models
from django.contrib.auth.models import User
import os
from datetime import datetime

def archivo_solicitud_path(instance, filename):
    # Formateo de la fecha de recepción
    fecha_recepcion = instance.solicitud.fecha_recepcion.strftime("%d-%m-%Y")
    
    # Formateo del nombre del archivo
    filename = f"{instance.solicitud.tipo_solicitud.nombre}_{instance.solicitud.folio}_{fecha_recepcion}_{filename}"
    
    # Construcción de la ruta de la carpeta con el nombre del folio
    return os.path.join(f"oirs/archivos/{instance.solicitud.folio}", filename)

class TipoSolicitud(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class ViaIngreso(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Area(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Sector(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Genero(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class EstadoRespuesta(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class TipoRespuesta(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Atingencia(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class SolicitudOIRS(models.Model):
    tipo_solicitud = models.ForeignKey(TipoSolicitud, on_delete=models.CASCADE)
    folio = models.CharField(max_length=50, unique=True)
    via_ingreso = models.ForeignKey(ViaIngreso, on_delete=models.CASCADE)
    tema = models.CharField(max_length=255)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    fecha_recepcion = models.DateField()
    fecha_maxima_respuesta = models.DateField()
    fecha_respuesta_entregada = models.DateField(null=True, blank=True)
    fecha_envio_funcionario = models.DateField(null=True, blank=True)
    fecha_recepcion_descargo = models.DateField(null=True, blank=True)
    tipo_respuesta = models.ForeignKey(TipoRespuesta, on_delete=models.CASCADE)
    estado_respuesta = models.ForeignKey(EstadoRespuesta, on_delete=models.CASCADE)
    texto_solicitud = models.TextField()
    nombre_usuario = models.CharField(max_length=255)
    rut_usuario = models.CharField(max_length=12)
    funcionario_aludido = models.CharField(max_length=255)
    atingencia = models.ForeignKey(Atingencia, on_delete=models.CASCADE)
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ultima_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.folio} - {self.tipo_solicitud}"

class ArchivoSolicitud(models.Model):
    # Opciones para el campo descripcion
    DESCRIPCION_OPCIONES = [
        ("correo_enviado_funcionario", "Correo enviado a funcionario"),
        ("Solicitud", "Solicitud"),
        ("correo_recibido_funcionario", "Correo recibido de funcionario"),
        ("respuesta_enviada", "Respuesta enviada a usuario"),
        ("otro_documento", "Otro documento"),
    ]

    solicitud = models.ForeignKey(SolicitudOIRS, on_delete=models.CASCADE, related_name='archivos')
    archivo = models.FileField(upload_to=archivo_solicitud_path)
    descripcion = models.CharField(max_length=255, choices=DESCRIPCION_OPCIONES)
    fecha_carga = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.solicitud.folio} - {self.get_descripcion_display()}"