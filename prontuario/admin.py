from django.contrib import admin

# Register your models here.
from prontuario.models import *

admin.site.register(Prontuario)
admin.site.register(DadosMedicos)
admin.site.register(Procedimento)
admin.site.register(Anamnese)
admin.site.register(InfSaudeSistemica)