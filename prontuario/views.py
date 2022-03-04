from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from prontuario.models import DadosMedicos, Medicamentos, Saude, ExameFisicoIB, PlanoTratamento, \
    CondOclusal, Odontograma, PSR, Procedimento


class DadosMedicosUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login")
    model = DadosMedicos
    fields = ('temp_trat', 'causa', 'crm_med', 'tel_med', 'cont_urg', )
    template_name = "prontuario/prontuario_geral.html"
    success_url = reverse_lazy("pacientes")


class MedicamentosUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login")
    model = Medicamentos
    fields = "__all__"
    template_name = "prontuario/prontuario_geral.html"
    success_url = reverse_lazy("pacientes")


class SaudeUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login")
    extra_context = {'nome_pagina': 'Saúde'}
    model = Saude
    fields = "__all__"
    template_name = "prontuario/prontuario_geral.html"
    success_url = reverse_lazy("pacientes")


class ExameFisicoIBUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login")
    model = ExameFisicoIB
    fields = "__all__"
    template_name = "prontuario/prontuario_geral.html"
    success_url = reverse_lazy("pacientes")


class PlanoTratamentoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login")
    extra_context = {'nome_pagina': 'Plano Tratamento'}
    model = PlanoTratamento
    fields = "__all__"
    template_name = "prontuario/prontuario_geral.html"
    success_url = reverse_lazy("pacientes")


class CondOclusalUpadate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login")
    extra_context = {'nome_pagina': 'Cond Oclusal'}
    model = CondOclusal
    fields = "__all__"
    template_name = "prontuario/prontuario_geral.html"
    success_url = reverse_lazy("pacientes")


class OdontogramaUpadate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login")
    extra_context = {'nome_pagina': 'Odontograma'}
    model = Odontograma
    fields = "__all__"
    template_name = "prontuario/prontuario_geral.html"
    success_url = reverse_lazy("pacientes")


class PSRUpadate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login")
    extra_context = {'nome_pagina': 'PSR'}
    model = PSR
    fields = "__all__"
    template_name = "prontuario/prontuario_geral.html"
    success_url = reverse_lazy("pacientes")


class ProcedimentoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login")
    extra_context = {'nome_pagina': 'Procedimento'}
    model = Procedimento
    fields = "__all__"
    template_name = "prontuario/prontuario_geral.html"
    success_url = reverse_lazy("pacientes")