from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Paciente, Especialista, Departamento, Direccion
from .forms import PacienteForm, EspecialistaForm

# Vista para el registro de un nuevo usuario
# Vista para el registro de un nuevo usuario
# Vista para el registro de un nuevo usuario
def signup(request):
    if request.method == 'GET':
        departamentos = Departamento.objects.all()  # Obtiene todos los departamentos
        direcciones = Direccion.objects.all()  # Obtiene todas las direcciones
        return render(request, 'signup.html', {"form": UserCreationForm(), "departamentos": departamentos, "direcciones": direcciones})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    username=request.POST["username"], password=request.POST["password1"]
                )
                user.save()

                # Recoge los datos del formulario
                nombre_especialista = request.POST.get("nombres")
                apellido_paterno = request.POST.get("apellido_paterno")
                apellido_materno = request.POST.get("apellido_materno")
                telefono = request.POST.get("telefono")
                correo = request.POST.get("correo")
                especialidad = request.POST.get("especialidad")
                departamento_id = request.POST["departamento"]  # ID del departamento
                edad = request.POST.get("edad")
                direccion_id = request.POST["direccion"]  # ID de la dirección

                # Crea el objeto Especialista
                especialista = Especialista.objects.create(
                    user=user,
                    nombre_especialista=nombre_especialista,
                    apellido_paterno=apellido_paterno,
                    apellido_materno=apellido_materno,
                    telefono=telefono,
                    correo=correo,
                    especialidad=especialidad,
                    edad=edad,
                    direccion_idDireccion_id=direccion_id,  # Usa el ID de la dirección
                    departamento_id_departamento_id=departamento_id  # Usa el ID del departamento
                )
                especialista.save()

                login(request, user)
                return redirect('pacientes')
            except IntegrityError:
                return render(request, 'signup.html', {"form": UserCreationForm(), "error": "El usuario ya existe."})

        return render(request, 'signup.html', {"form": UserCreationForm(), "error": "No coinciden las contraseñas."})

# Vista para mostrar los pacientes pendientes (no completados)
@login_required
def pacientes(request):
    pacientes = Paciente.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'paciente.html', {"pacientes": pacientes})

# Vista para mostrar los pacientes completados
@login_required
def pacientes_completed(request):
    pacientes = Paciente.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'paciente.html', {"pacientes": pacientes})

# Vista para crear un nuevo paciente
@login_required
def create_paciente(request):
    if request.method == "GET":
        return render(request, 'create_paciente.html', {"form": PacienteForm()})
    else:
        try:
            form = PacienteForm(request.POST)  # Carga los datos del formulario
            new_paciente = form.save(commit=False)  # Crea un nuevo paciente, pero no lo guarda aún
            new_paciente.user = request.user  # Asigna el paciente al usuario actual
            new_paciente.save()  # Guarda el paciente en la base de datos
            return redirect('pacientes')  # Redirige a la lista de pacientes
        except ValueError:
            return render(request, 'create_paciente.html', {"form": PacienteForm(), "error": "Surgió un error al crear al paciente."})

# Vista para mostrar la página de inicio
def home(request):
    return render(request, 'home.html')

# Vista para cerrar la sesión de un usuario
@login_required
def signout(request):
    logout(request)  # Cierra la sesión
    return redirect('home')  # Redirige a la página de inicio

# Vista para el inicio de sesión
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm()})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm(), "error": "Nombre de usuario o contraseña incorrectos."})

        login(request, user)
        return redirect('pacientes')

# Vista para mostrar los detalles de un paciente específico
@login_required
def paciente_detail(request, paciente_id):
    if request.method == 'GET':
        paciente = get_object_or_404(Paciente, pk=paciente_id, user=request.user)
        form = PacienteForm(instance=paciente)
        return render(request, 'paciente_detail.html', {'paciente': paciente, 'form': form})
    else:
        try:
            paciente = get_object_or_404(Paciente, pk=paciente_id, user=request.user)
            form = PacienteForm(request.POST, instance=paciente)
            form.save()  # Guarda los cambios en la base de datos
            return redirect('pacientes')
        except ValueError:
            return render(request, 'paciente_detail.html', {'paciente': paciente, 'form': form, 'error': 'Error al actualizar al paciente.'})

# Vista para marcar un paciente como completado
@login_required
def complete_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id, user=request.user)
    if request.method == 'POST':
        paciente.datecompleted = timezone.now()
        paciente.save()
        return redirect('pacientes')

# Vista para eliminar un paciente
@login_required
def delete_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id, user=request.user)
    if request.method == 'POST':
        paciente.delete()
        return redirect('pacientes')

# Perfil
@login_required
def perfil_doc(request):
    user = request.user
    try:
        doctor = Especialista.objects.get(user=user)
        context = {
            'nombre_especialista': doctor.nombre_especialista,
            'apellido_paterno': doctor.apellido_paterno,
            'apellido_materno': doctor.apellido_materno,
            'edad': doctor.edad,
            'departamento': doctor.departamento,
            'username': user.username,
        }
        return render(request, 'perfil_especialista.html', context)
    except Especialista.DoesNotExist:
        return redirect('error_page')

def error_page(request):
    return render(request, 'error_page.html')

def homeDoctor(request):
    return render(request, 'homeDoctor.html')
