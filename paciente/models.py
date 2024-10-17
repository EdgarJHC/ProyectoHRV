from django.db import models
from django.contrib.auth.models import User

# Clase Paciente que representa los datos de un paciente en la base de datos
class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)  # Asegúrate de que este campo sea autoincremental
    nombre_paciente = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(max_length=100)
    sexo = models.CharField(max_length=10)  # Puedes ajustar el max_length según sea necesario
    fecha_nacimiento = models.DateField()  # Cambié a DateField para representar fechas
    direccion_idDireccion = models.ForeignKey('Direccion', on_delete=models.CASCADE)  # Asegúrate de tener un modelo Direccion
    uso_de_medicamentos = models.BooleanField(default=False)
    actividad_fisica = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Mantener la relación con el modelo User

    def __str__(self):
        return f"{self.nombre_paciente} {self.apellido_paterno} - {self.user.username}"

    class Meta:
        db_table = 'paciente'

class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nombre_estado = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_estado

    class Meta:
        db_table = 'estado'

class Direccion(models.Model):
    idDireccion = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=255)
    colonia = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    Estado_id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)  # Relación con el modelo Estado

    def __str__(self):
        return f"{self.calle}, {self.colonia}, {self.ciudad}, {self.pais}, {self.Estado_id_estado}"
    
    class Meta:
        db_table = 'direccion'




class Departamento(models.Model):
    id_departamento = models.AutoField(primary_key=True)
    departamento = models.CharField(max_length=45)  # Asegúrate de que este campo exista

    def __str__(self):
        return self.departamento

    class Meta:
        db_table = 'departamento'


class Especialista(models.Model):
    id_especialista = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relación con el modelo User
    nombre_especialista = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(max_length=100)
    especialidad = models.CharField(max_length=100)
    edad = models.IntegerField()
    direccion_idDireccion = models.ForeignKey('Direccion', on_delete=models.CASCADE)  # Asegúrate de tener un modelo Direccion
    departamento_id_departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)  # Cambiado a ForeignKey

    def __str__(self):
        return (f"{self.id_especialista} - {self.nombre_especialista} {self.apellido_paterno} {self.apellido_materno}, "
                f"Edad: {self.edad}, Teléfono: {self.telefono}, Correo: {self.correo}, "
                f"Especialidad: {self.especialidad}, Departamento: {self.departamento_id_departamento}")

    class Meta:
        db_table = 'especialista'