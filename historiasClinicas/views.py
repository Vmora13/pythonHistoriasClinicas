from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from .models import HistoriaClinica, Paciente,Medico, CentroMedico
from .serializers import HistoriaClinicaSerializers, PacienteSerializers,MedicoSerializers, CentroMedicoSerializers

# Create your views here.
class HistoriaClinicaView (viewsets.ModelViewSet):
    queryset = HistoriaClinica.objects.all()
    serializer_class = HistoriaClinicaSerializers


class PacienteView (viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializers
    
class MedicoView (viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializers

class CentroMedicoView (viewsets.ModelViewSet):
    queryset = CentroMedico.objects.all()
    serializer_class = CentroMedicoSerializers