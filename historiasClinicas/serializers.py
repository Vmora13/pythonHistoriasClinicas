from rest_framework import routers, serializers, viewsets
from .models import *

class HistoriaClinicaSerializers (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HistoriaClinica
        fields = ['id', 'fecha', 'evento']
        pass

class PacienteSerializers (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paciente
        fields = ['id', 'nombre', 'cedula', 'ciudad', 'direccion', 'telefono' ]
        pass

class MedicoSerializers (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medico
        fields = ['id', 'nombre', 'cedula', 'tarjetaProfesional', 'Especialidad', 'paciente']
        pass

class CentroMedicoSerializers (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CentroMedico
        fields = ['id', 'nombre', 'ciudad', 'direccion', 'telefono', 'paciente', 'medico']
        pass
