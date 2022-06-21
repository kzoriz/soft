import self
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView

import prontuario
from prontuario.models import *
from django.contrib import messages
from django.urls import reverse


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


def anamnese_detalhes(request, pk=None):
    object = Anamnese.objects.get(pk=pk)
    #prontuario = Prontuario.objects.get(pk=pk)
    context = {
        'object': object,
        'prontuario': prontuario,
    }
    return render(request, 'prontuario/anamnese_detalhes.html', context)


class AnamneseUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy("login")
    extra_context = {'nome_pagina': 'Anamnese'}
    model = Anamnese
    fields = ['anamnese', ]
    template_name = "prontuario/anamnese_editar.html"
    #success_url = reverse_lazy("pacientes")
    #success_url = reverse_lazy("anamnese_detalhes", kwargs={'slug': self.slug})
    #success_message = "Atualizado"
    #context_object_name = 'anamnese'


class InfSaudeSistemicaUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy("login")
    extra_context = {'nome_pagina': 'Informção de Saúde Sistemica'}
    model = InfSaudeSistemica
    #fields = "__all__"
    fields = ['antecedentes_familiares', 'medicamentos_em_uso', 'cirurgias_anteriores', 'problemas_cardiacos',
              'problemas_gastrointestinais', 'alteracoes_sanguineas', 'enfermidades_osseas', 'problemas_pulmonares',
              'alergias', 'habitos', 'observacao']
    template_name = "prontuario/inf_saude_sistemica_editar.html"


def inf_saude_sistemica_detalhes(request, pk=None):
    object = InfSaudeSistemica.objects.get(pk=pk)
    context = {
        'object': object,
    }
    return render(request, 'prontuario/inf_saude_sistemica.html', context)








