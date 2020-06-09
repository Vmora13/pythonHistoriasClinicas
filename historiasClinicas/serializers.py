from rest_framework import routers, serializers, viewsets
from .models import *

class HistoriaClinicaSerializers (serializers.ModelSerializer):
    class Meta:
        model = HistoriaClinica
        fields = ['id', 'fecha', 'evento']
        pass

class PacienteSerializers (serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['id', 'nombre', 'cedula', 'ciudad', 'direccion', 'telefono', 'historiaClinica' ]
        pass

class MedicoSerializers (serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ['id', 'nombre', 'cedula', 'tarjetaProfesional', 'especialidad', 'paciente']
        pass

class CentroMedicoSerializers (serializers.ModelSerializer):
    class Meta:
        model = CentroMedico
        fields = ['id', 'nombre', 'ciudad', 'direccion', 'telefono', 'paciente', 'medico']
        pass
