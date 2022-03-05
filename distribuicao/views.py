from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from distribuicao.forms import DistribuicaoForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .models import Distribuicao, Disciplina
# Create your views here.
def distribuir_paciente_index(request):
    return render(request, "distribuir_paciente/distribuir_paciente_index.html" )


class DistribuicaoCreateView(CreateView):
    model = Distribuicao
    fields = "__all__"
    template_name = "distribuir_paciente/distribuicao.html"
    success_url = reverse_lazy("distribuir_pacientes_menu")

class DisciplinaCreateView(CreateView):
    model = Disciplina
    fields = "__all__"
    template_name = "distribuir_paciente/cadastro_disciplina.html"
    success_url = reverse_lazy("opcoes")

def distribuicoes(request):
    todas_distribuicoes = Distribuicao.objects.all()

    context = {
        "nome_pagina": "DISTRIBUIÇÕES",
        "todas_distribuicoes": todas_distribuicoes,

    }
    return render(request, "distribuir_paciente/distribuicoes.html", context)

def disciplinas(request):
    todas_disciplinas = Disciplina.objects.all()

    context = {
        "nome_pagina": "DISCIPLINAS",
        "todas_disciplinas": todas_disciplinas,

    }
    return render(request, "distribuir_paciente/disciplinas.html", context)

def disciplina_detalhes(request, pk = None):
    disciplina = Disciplina.objects.get(pk=pk)
    context = {
        'disciplina': disciplina
    }
    return render(request, 'distribuir_paciente/disciplina_detalhes.html', context)

class DisciplinaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login")
    model = Disciplina
    fields = "__all__"
    template_name = "distribuir_paciente/disciplina_editar.html"
    success_url = reverse_lazy("disciplinas")

class DisciplinaDelete(LoginRequiredMixin,DeleteView):
    login_url = reverse_lazy("login")
    model = Disciplina
    template_name = "distribuir_paciente/disciplina_delete.html"
    success_url = reverse_lazy("disciplinas")