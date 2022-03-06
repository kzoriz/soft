from django.db import models
from pacientes.models import Paciente


C_CHOICES = [
    ('SIM', 'SIM'),
    ('NAO', 'NÃO'),
]


class Prontuario(models.Model):
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    num_prontuario = models.CharField("NumProntuario", max_length=200)

    def __str__(self):
        return self.num_prontuario


class DadosMedicos(models.Model):

    prontuario = models.OneToOneField(Prontuario, on_delete=models.CASCADE)
    temp_trat = models.CharField("Tempo de Tratamento", max_length=50, blank=True)
    causa = models.CharField("Causa", max_length=50, blank=True)
    crm_med = models.CharField("CRM Medico", max_length=50, blank=True)
    tel_med = models.CharField("Telefone Medico", max_length=25, blank=True)
    cont_urg = models.CharField("Contato de Urgencia", max_length=25, blank=True)

    def __str__(self):
        return self.prontuario.paciente.nome


class Medicamentos(models.Model):

    PRONTUARIO_CHOICES = [
        ('Med1', 'Medicamnto1'),
        ('Med2', 'Medicamnto2'),
        ('Med3', 'Medicamnto3'),
        ('Med4', 'Medicamnto4'),
        ('Med5', 'Medicamnto5'),
    ]

    prontuario = models.OneToOneField(Prontuario, on_delete=models.CASCADE)
    medicamento = models.CharField("Medicamento", max_length=100, choices=PRONTUARIO_CHOICES, blank=True)
    cirur_real = models.CharField("Cirurgia Realizada", max_length=50, blank=True)
    dst = models.CharField("DST", max_length=50, blank=True)
    anticoncepcional = models.CharField("Anticoncepcional", max_length=50, blank=True)
    cardiopatia = models.CharField("Cardiopatias", max_length=50, blank=True)
    prob_gastri = models.CharField("Problemas Gastricos", max_length=50, blank=True)
    prob_pulmo = models.CharField("Problemas Pulmonares", max_length=50, blank=True)
    alt_sang = models.CharField("Alterações Sanguineas", max_length=50, blank=True)
    enf_ossea_infla = models.CharField("Infermidades Osséa Inflamatorias", max_length=50, blank=True)
    habitos = models.CharField("Hábitos", max_length=50, blank=True)
    alergias = models.CharField("Alergias", max_length=50, blank=True)

    def __str__(self):
        return self.prontuario


class Saude(models.Model):

    prontuario = models.OneToOneField(Prontuario, on_delete=models.CASCADE)
    diabetes = models.CharField("Diabetes", max_length=3, choices=C_CHOICES)
    gravida = models.CharField("Grávida", max_length=3, choices=C_CHOICES)
    plan_grav = models.CharField("Planeja Gravidez", max_length=3, choices=C_CHOICES)
    hipertensao = models.CharField("Hipertensão", max_length=3, choices=C_CHOICES)
    sangramento = models.CharField("Sangramento", max_length=3, choices=C_CHOICES)
    epilepsia = models.CharField("Epilepsia", max_length=3, choices=C_CHOICES)
    prob_ren = models.CharField("Problemas Renais", max_length=3, choices=C_CHOICES)
    doenc_mental = models.CharField("Doença Mental", max_length=3, choices=C_CHOICES)
    rad_terapia = models.CharField("Rádio Terapia", max_length=3, choices=C_CHOICES)
    qui_terapia = models.CharField("Quimioterapia", max_length=3, choices=C_CHOICES)
    hepatite = models.CharField("Hepatite", max_length=3, choices=C_CHOICES)
    articulacao = models.CharField("Articulações", max_length=3, choices=C_CHOICES)
    protese = models.CharField("Prótese", max_length=3, choices=C_CHOICES)
    hiv = models.CharField("HIV", max_length=3, choices=C_CHOICES)
    fumante = models.CharField("Fumante", max_length=3, choices=C_CHOICES)
    herpes = models.CharField("Herpes", max_length=3, choices=C_CHOICES)
    bebida = models.CharField("Bebida", max_length=3, choices=C_CHOICES)
    inf_add = models.TextField("Informações Adicionais")


class ExameFisicoIB(models.Model):
    prontuario = models.OneToOneField(Prontuario, on_delete=models.CASCADE)
    atm = models.CharField("ATM", max_length=50, blank=True)
    lab_sup = models.CharField("Labio Superior", max_length=50, blank=True)
    lab_inf = models.CharField("LabioInferior", max_length=50, blank=True)
    com_labial = models.CharField("Comissura Labial", max_length=50, blank=True)
    muc_jugal = models.CharField("Mucosa Jugal", max_length=50, blank=True)
    palato_duro = models.CharField("Palato Duro", max_length=50, blank=True)
    palato_mole = models.CharField("Palato Mole", max_length=50, blank=True)
    tonsilas = models.CharField("Tonsilas", max_length=50, blank=True)
    hig_oral = models.CharField("Higiene Oral", max_length=50, blank=True)
    sang_gengival = models.CharField("Sangramento Gengival", max_length=50, blank=True)
    calculo = models.CharField("Cálculo", max_length=50, blank=True)


class PlanoTratamento(models.Model):
    prontuario = models.OneToOneField(Prontuario, on_delete=models.CASCADE)
    reg_dente = models.CharField("Região do Dente", max_length=50, blank=True)
    procedimento = models.CharField("Procedimento", max_length=50, blank=True)


class CondOclusal(models.Model):
    prontuario = models.OneToOneField(Prontuario, on_delete=models.CASCADE)
    tipo_co = models.CharField("Tipo CO", max_length=100, blank=True)


class Odontograma(models.Model):
    prontuario = models.OneToOneField(Prontuario, on_delete=models.CASCADE)
    dente = models.CharField("Dente", max_length=100, blank=True)
    condicao = models.CharField("Condição", max_length=100, blank=True)


class PSR(models.Model):
    prontuario = models.OneToOneField(Prontuario, on_delete=models.CASCADE)
    sextante = models.CharField("Sextante", max_length=100, blank=True)
    classificacao = models.CharField("Classificação", max_length=100, blank=True)


class Procedimento(models.Model):
    prontuario = models.CharField("NumProntuario", max_length=200)
    cpf = models.CharField("CPF", max_length=100, blank=True)
    reg_dente = models.CharField("Região do Dente", max_length=50, blank=True)
    procedimento = models.CharField("Procedimento", max_length=50, blank=True)

    def __str__(self):
        return self.cpf
