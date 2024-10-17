from django.forms import ModelForm
from .models import Paciente, Especialista  # Importar ambos modelos
from django import forms

# Clase PacienteForm que se basa en el modelo Paciente.
class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'nombre_paciente', 
            'apellido_paterno', 
            'apellido_materno', 
            'telefono', 
            'correo', 
            'sexo', 
            'fecha_nacimiento', 
            'direccion_idDireccion', 
            'uso_de_medicamentos', 
            'actividad_fisica', 
            'user'  # Asegúrate de que el usuario se asigne correctamente
        ]


# Clase EspecialistaForm que se basa en el modelo Especialista.
class EspecialistaForm(forms.ModelForm):
    class Meta:
        model = Especialista
        fields = [
            'nombre_especialista', 
            'apellido_paterno', 
            'apellido_materno', 
            'telefono', 
            'correo', 
            'especialidad', 
            'edad', 
            'direccion_idDireccion', 
            'departamento_id_departamento',  # Este campo ahora debe ser correcto
            'user'  # Asegúrate de que el usuario se asigne correctamente
        ]
