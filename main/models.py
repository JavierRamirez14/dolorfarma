from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Patologia(models.Model):

    diagnostico_opciones = [('Con diagnóstico', 'Con diagnóstico'), ('Sin diagnóstico', 'Sin diagnóstico')]

    titulo = models.CharField(max_length=100, default='None')
    dolor = models.CharField(max_length=100, default='None')
    cuerpo = models.CharField(max_length=100, default='None')
    diagnostico = models.CharField(max_length=30, choices=diagnostico_opciones, default='Con diagnóstico')
    descripcion = models.TextField(default='Sin descripción')
    imagen = models.ImageField(upload_to='patologia_imagenes/', null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} - {self.dolor} - {self.cuerpo}"

class Documento(models.Model):
    titulo = models.CharField(max_length=100, default='None')
    duracion = models.CharField(max_length=100, default='None')
    documento= models.TextField(blank=True, null=True, default='None')

    def __str__(self):
        return f"{self.titulo} - {self.duracion}"
    

class Consulta(models.Model):
    id = models.AutoField(primary_key=True)  # Identificador autoincremental
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    dolor = models.CharField(max_length=100, default='None')
    cuerpo = models.CharField(max_length=100, default='None')
    patologia = models.CharField(max_length=200, default='None')
    intensidad = models.CharField(max_length=100, default='None')
    duracion = models.CharField(max_length=100, default='None')
    fecha = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'ID: {self.id}'
    

class Numeros_Farmacia(models.Model):
    farmacia = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    telefono = models.CharField(max_length=9, default='None')
    notificaciones = models.BooleanField(default=False)
    