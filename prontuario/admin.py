from django.contrib import admin

# Register your models here.
from prontuario.models import Prontuario, DadosMedicos, Procedimento

admin.site.register(Prontuario)
admin.site.register(DadosMedicos)
admin.site.register(Procedimento)