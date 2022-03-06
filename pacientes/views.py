from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from prontuario.models import Prontuario, DadosMedicos, Medicamentos, Saude, ExameFisicoIB, PlanoTratamento, \
    CondOclusal, Odontograma, PSR, Procedimento
from pacientes.forms import PacienteForm, PacienteInfantilForm
from django.views.generic.edit import UpdateView, DeleteView
from pacientes.models import Paciente, PacienteInfantil
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime


@login_required
def registrar_paciente(request):
    form = PacienteForm()
    x = datetime.datetime.now()
    # a = x.strftime("%H")
    b = x.strftime("%M")
    c = x.strftime("%S")
    d = x.strftime("%Y")
    # e = x.strftime("%m")
    # f = x.strftime("%d")
    if request.method == "POST":
        form = PacienteForm(request.POST)
        if form.is_valid():
            paciente = form.save(commit=False)
            paciente.save()
            u = Prontuario(paciente=paciente, num_prontuario=b+c+d)
            u.save()
            v = DadosMedicos(prontuario=u)
            v.save()
            w = Medicamentos(prontuario=u)
            w.save()
            p = Saude(prontuario=u)
            p.save()
            y = ExameFisicoIB(prontuario=u)
            y.save()
            z = PlanoTratamento(prontuario=u)
            z.save()
            r = CondOclusal(prontuario=u)
            r.save()
            m = Odontograma(prontuario=u)
            m.save()
            n = PSR(prontuario=u)
            n.save()
            o = Procedimento(
                prontuario=u,
                cpf=paciente.cpf,
            )
            o.save()
            messages.success(request, "Paciente registrado com sucesso")
            return redirect("inicio")
    context = {
        "nome_pagina": "Registrar Paciente",
        "form": form,
        "messages": messages.success,
    }
    return render(request, "pacientes/paciente_registrar.html", context)


@login_required
def registrar_paciente_inf(request):
    form = PacienteInfantilForm
    if request.method == "POST":
        form = PacienteInfantilForm(request.POST)
        if form.is_valid():
            paciente_inf = form.save(commit=False)
            paciente_inf.save()
            messages.success(request, "Paciente infantil registrado com sucesso")
            return redirect("inicio")
    context = {
        "form": form,
        "messages": messages.success,
    }
    return render(request, "pacientes/paciente_registrar_inf.html", context=context)


@login_required
def pacientes(request):
    todos_pacientes = Paciente.objects.order_by("nome")
    todos_dados_medicos = DadosMedicos.objects.all()
    todos_pacientes_inf = PacienteInfantil.objects.order_by("-id")

    context = {
        "nome_pagina": "Pacientes",
        "todos_pacientes": todos_pacientes,
        "todos_pacientes_inf": todos_pacientes_inf,
        "dados_medicos": todos_dados_medicos,

    }
    return render(request, "pacientes/pacientes.html", context)


def agenda(request):
    context = {
    }
    return render(request, "pacientes/agenda.html", context)


@login_required
def opcoes(request):
    context = {
    }
    return render(request, "pacientes/opcoes.html", context)


@login_required
def paciente_detalhes(request, pk=None):
    instance = Paciente.objects.get(pk=pk)
    prontuario = Prontuario.objects.get(pk=pk)
    dados_med = DadosMedicos.objects.get(pk=pk)
    med = Medicamentos.objects.get(pk=pk)
    saude = Saude.objects.get(pk=pk)
    exam = ExameFisicoIB.objects.get(pk=pk)
    plan = PlanoTratamento.objects.get(pk=pk)
    cond = CondOclusal.objects.get(pk=pk)
    odon = Odontograma.objects.get(pk=pk)
    psr = PSR.objects.get(pk=pk)
    proc = Procedimento.objects.get(pk=pk)
    context = {
        'object': instance,
        'prontuario': prontuario,
        'dados_med': dados_med,
        'med': med,
        'sau': saude,
        'exam': exam,
        'plan': plan,
        'cond': cond,
        'odon': odon,
        'psr': psr,
        'proc': proc,
    }
    return render(request, 'pacientes/paciente_detalhes.html', context)


@login_required
def paciente_detalhes_inf(request, pk=None):
    instance = PacienteInfantil.objects.get(pk=pk)
    context = {
        'object': instance
    }
    return render(request, 'pacientes/paciente_detalhes_inf.html', context)


class PacienteUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login")
    model = Paciente
    fields = "__all__"
    template_name = "pacientes/paciente_editar.html"
    success_url = reverse_lazy("pacientes")


class PacienteInfantilUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login")
    model = PacienteInfantil
    fields = "__all__"
    template_name = "pacientes/paciente_editar_inf.html"
    success_url = reverse_lazy("pacientes")


class PacienteDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy("login")
    model = Paciente
    template_name = "pacientes/paciente_delete.html"
    success_url = reverse_lazy("pacientes")


class PacienteInfantilDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy("login")
    model = PacienteInfantil
    template_name = "pacientes/paciente_delete_inf.html"
    success_url = reverse_lazy("pacientes")


@login_required
def inicio(request):
    return render(request, "pacientes/pacientes/inicio.html")


@login_required
def registrar_paciente_2(request):
    return render(request, "pacientes/pacientes_menu.html")
