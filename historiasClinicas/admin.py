from django.contrib import admin
from .models    import *
# Register your models here.
admin.site.register(CentroMedico)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(HistoriaClinica)