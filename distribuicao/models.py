from django.db import models
from pacientes.models import Paciente
from usuarios.models import Discente, Docente



class Disciplina(models.Model):
    PERIODO = [
        ('1º', '1º'),
        ('2º', '2º'),
        ('3º', '3º'),
        ('4º', '4º'),
        ('5º', '5º'),
        ('6º', '6º'),
        ('7º', '7º'),
        ('8º', '8º'),
        ('9º', '9º'),
        ('10º', '10º'),

    ]
    nome = models.CharField(verbose_name="Nome Disciplina", max_length=200)
    codigo = models.CharField(verbose_name="CodDisc", max_length=200)
    periodo = models.CharField(verbose_name="Periodo", max_length=3, choices=PERIODO)
    matricula_docente = models.ForeignKey(Docente, verbose_name="MatDocente", on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.nome
class Distribuicao(models.Model):

    PROCEDIMENTO = [
        ('restaurações', 'RESTAURAÇÃO'),
        ('aplicação de flúor', 'APLICAÇÃO FLUOR'),
        ('tratamentos de canal', 'TRATAMENTO CANAL'),
        ('tratamento de bruxismo', 'TRATAMENTO BRUXISMO'),

    ]

    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE, null=True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.SET_NULL, null=True)
    discente = models.ForeignKey(Discente, on_delete=models.SET_NULL, null=True)
    docente = models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True)
    data_atendimento = models.DateTimeField(verbose_name="Data/Hora Atendimento")
    procedimento = models.CharField(verbose_name="Procedimento", max_length=200, choices=PROCEDIMENTO)


    def __str__(self):
        return self.procedimento


