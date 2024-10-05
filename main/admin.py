from django.contrib import admin

from .models import Patologia, Consulta, Documento, Numeros_Farmacia

admin.site.register(Patologia)
admin.site.register(Documento)
admin.site.register(Consulta)
admin.site.register(Numeros_Farmacia)