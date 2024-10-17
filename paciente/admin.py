from django.contrib import admin  # Importa el módulo admin de Django para gestionar la interfaz de administración
from .models import *


# Registra el modelo Paciente y su clase administrativa asociada en la interfaz de administración de Django
admin.site.register(Paciente)  # Esto permite que el modelo Paciente sea gestionado a través de la interfaz de administración
admin.site.register(Especialista)
admin.site.register(Departamento)