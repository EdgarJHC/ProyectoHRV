# Generated by Django 3.2.8 on 2024-10-25 00:59

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id_departamento', models.AutoField(primary_key=True, serialize=False)),
                ('departamento', models.CharField(blank=True, max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id_paciente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_paciente', models.CharField(blank=True, max_length=45, verbose_name='Nombre del paciente')),
                ('apellido_paterno', models.CharField(blank=True, max_length=45, verbose_name='Apellido paterno')),
                ('apellido_materno', models.CharField(blank=True, max_length=45, verbose_name='Apellido materno')),
                ('telefono', models.CharField(blank=True, max_length=15, verbose_name='Telefono')),
                ('correo', models.CharField(blank=True, max_length=45, verbose_name='Correo electrónico')),
                ('sexo', models.CharField(blank=True, max_length=15, verbose_name='Sexo')),
                ('fecha_nacimiento', models.DateField(blank=True, verbose_name='Fecha Nacimiento')),
                ('imc', models.FloatField()),
                ('uso_de_medicamentos', models.CharField(blank=True, max_length=100, null=True, verbose_name='Medicamentos')),
                ('actividad_fisica', models.CharField(blank=True, max_length=100, null=True, verbose_name='Actividad física')),
                ('foto', models.ImageField(null=True, upload_to=' ', verbose_name='Fotografía del paciente')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Especialista',
            fields=[
                ('id_especialista', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_especialista', models.CharField(max_length=100)),
                ('apellido_paterno', models.CharField(max_length=100)),
                ('apellido_materno', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('correo', models.EmailField(max_length=100)),
                ('especialidad', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField(blank=True, verbose_name='Fecha Nacimiento')),
                ('departamento_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paciente.departamento')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ECG',
            fields=[
                ('id_ecg', models.AutoField(primary_key=True, serialize=False)),
                ('archivo_ecg', models.FileField(upload_to='archivo_ecg/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['txt', 'csv'])])),
                ('fecha_informe', models.DateTimeField(auto_now_add=True)),
                ('comentarios', models.TextField()),
                ('homoclave', models.CharField(blank=True, max_length=64, null=True, unique=True)),
                ('paciente', models.ForeignKey(db_column='ID_PACIENTE', on_delete=django.db.models.deletion.CASCADE, to='paciente.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='AnalisisDominioTiempo',
            fields=[
                ('id_analisis_tiempo', models.AutoField(primary_key=True, serialize=False)),
                ('nni_mean', models.FloatField()),
                ('nni_min', models.FloatField()),
                ('nni_max', models.FloatField()),
                ('hr_mean', models.FloatField()),
                ('hr_min', models.FloatField()),
                ('hr_max', models.FloatField()),
                ('std_hr', models.FloatField()),
                ('nni_diff_mean', models.FloatField()),
                ('nni_diff_min', models.FloatField()),
                ('nni_diff_max', models.FloatField()),
                ('std_rr', models.FloatField()),
                ('ssdn_index', models.FloatField()),
                ('sdann', models.FloatField()),
                ('rmssd', models.FloatField()),
                ('sdsd', models.FloatField(default=0.0)),
                ('nn50', models.FloatField()),
                ('pnns50', models.FloatField()),
                ('nn20', models.FloatField()),
                ('rr_mean', models.FloatField()),
                ('total_intervalos_rr', models.IntegerField()),
                ('histograma_rr', models.ImageField(null=True, upload_to='media/')),
                ('histograma_hr', models.ImageField(null=True, upload_to='media/')),
                ('histograma_nni', models.ImageField(null=True, upload_to='media/')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('paciente', models.ForeignKey(db_column='id_paciente', on_delete=django.db.models.deletion.CASCADE, to='paciente.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='AnalisisDominioFrecuencia',
            fields=[
                ('id_analisis_frecuencia', models.AutoField(primary_key=True, serialize=False)),
                ('tasa_muestreo', models.IntegerField()),
                ('power_high_frequency', models.FloatField()),
                ('power_low_frequency', models.FloatField()),
                ('potencia_total', models.FloatField()),
                ('lh_hf', models.FloatField()),
                ('espectro_frecuencias', models.ImageField(null=True, upload_to='media/')),
                ('psd', models.ImageField(null=True, upload_to='media/')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('ecg', models.ForeignKey(db_column='ID_ECG', on_delete=django.db.models.deletion.CASCADE, to='paciente.ecg')),
                ('paciente', models.ForeignKey(db_column='id_paciente', on_delete=django.db.models.deletion.CASCADE, to='paciente.paciente')),
            ],
        ),
    ]
