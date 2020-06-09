from django.db import models

# Create your models here.
class HistoriaClinica (models.Model):
    fecha = models.DateField()
    evento = models.CharField(max_length=20)

class Paciente (models.Model):
    nombre = models.CharField(max_length=20)
    cedula = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=20)
    direccion = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)

    historiaClinica = models.ForeignKey(to=HistoriaClinica,on_delete=models.CASCADE, null=True, blank=True)

class Medico (models.Model):
    nombre = models.CharField(max_length=20)
    cedula = models.CharField(max_length=20)
    tarjetaProfesional = models.IntegerField()
    especialidad = models.CharField(max_length=20)

    paciente = models.ForeignKey(to=Paciente, on_delete=models.CASCADE, null=False, blank=False)


class CentroMedico (models.Model):
    nombre = models.CharField(max_length=15)
    ciudad = models.CharField(max_length =20)
    direccion = models.CharField(max_length=20)
    telefono = models.IntegerField()

    paciente = models.ForeignKey(to=Paciente,on_delete=models.CASCADE, null=False, blank=False)
    medico = models.ForeignKey(to=Medico, on_delete=models.CASCADE, null=False, blank=False)

    