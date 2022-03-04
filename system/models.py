from django.db import models

# Create your models here.
SEXO_BIOLOGICO = [
    ("MASCULINO", "masculino"),
    ("FEMININO", "feminino"),
]
RACA = [
    ("BRANCO", "branco"),
    ("PARDO", "pardo"),
    ("PRETO", "preto"),
    ("INDIGENA", "indigena"),
    ("AMARELO", "amarelo"),
]
ESTADO_CIVIL = [
    ("SOLTEIRO", "Solteiro"),
    ("CASADO", "Casado"),
    ("SEPARADO", "Separado"),
    ("DIVORCIADO", "Divorciado"),
    ("VIUVO", "Viúvo"),
]
A_F = [
    ("S", "Sim"),
    ("N", "Não"),
]
GRAU_INSTRUCAO = [
    ('NIVEL 1', (
        ('ANALFABETO', 'Analfabeto'),
        ('5º_ANO_INCOMPLETO', 'Até 5º Ano Incompleto'),
        ('5º_ANO_COMPLETO', 'Até 5º Ano completo'),
        ('6º_AO_9º_Ano_do_Fundamental', '6º ao 9º Ano do Fundamental'),
    )
     ),
    ('NIVEL 2', (
        ('Fundamental_Completo', 'Fundamental Completo'),
        ('Médio Incompleto', 'Médio Incompleto'),
    )
     ),
    ('NIVEL 3', (
        ('Médio Completo', 'Médio Completo'),
        ('Superior Incompleto', 'Superior Incompleto'),
    )
     ),
    ('NIVEL 4', (
        ('Superior Completo', 'Superior Completo'),
    )
     ),
    ('NIVEL 5', (
        ('Mestrado', 'Mestrado'),
        ('Doutorado', 'Doutorado'),
    )
     ),
]
UF_CHOICES = (
    ('AC', 'Acre'),
    ('AM', 'Amazonas'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranão'),
    ('MG', 'Minas Gerais'),
    ('MS', 'Mato Grosso do Sul'),
    ('MT', 'Mato Grosso'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PE', 'Pernanbuco'),
    ('PI', 'Piauí'),
    ('PR', 'Paraná'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('RS', 'Rio Grande do Sul'),
    ('SC', 'Santa Catarina'),
    ('SE', 'Sergipe'),
    ('SP', 'São Paulo'),
    ('TO', 'Tocantins')
)
class Paciente(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=200)
    nome_social = models.CharField(verbose_name="Nome Social", max_length=200, blank=True)
    data_nascimento =models.DateField(verbose_name="Data de Nascimento", auto_now=False, auto_now_add=False)
    sexo_biologico = models.CharField(verbose_name="Sexo Biologico", max_length=9, choices=SEXO_BIOLOGICO)
    rg = models.CharField(verbose_name="RG", max_length=16, blank=True)
    cpf = models.CharField(verbose_name="CPF", max_length=14, default="86777069178")
    raca = models.CharField(verbose_name="Raça", max_length=9, choices=RACA)
    estado_civil = models.CharField(verbose_name="Estado Civil", max_length=10, choices=ESTADO_CIVIL)
    grau_instrucao = models.CharField(verbose_name="Grau de Instrução", max_length=200, choices=GRAU_INSTRUCAO)
    endereco = models.CharField(verbose_name="Endereço", max_length=200, default="Rua Antônio Barbosa Sobrinho")
    cep = models.CharField(verbose_name="CEP", max_length=9, default="39651970")
    bairro = models.CharField(verbose_name="Bairro", max_length=200,default="Centro")
    cidade = models.CharField(verbose_name="Cidade", max_length=200, default="Ribeirão da Folha")
    uf = models.CharField(verbose_name="UF", max_length=2, choices=UF_CHOICES)
    telefone_celular = models.CharField(verbose_name="Telefone Celular", max_length=11, default="33991514101")
    antecedentes_familiares = models.TextField(verbose_name="Antecedente Familiares", default="Dados de importância para a história clínica.")

    def __str__(self):
        return self.nome

class PacienteInfantil(models.Model):
    responsavel = models.CharField(verbose_name="Reponsavel", max_length=200)
    nome = models.CharField(verbose_name="Nome", max_length=200)
    nome_social = models.CharField(verbose_name="Nome Social", max_length=200, blank=True)
    data_nascimento = models.DateField(verbose_name="Data de Nascimento", auto_now=False, auto_now_add=False)
    sexo_biologico = models.CharField(verbose_name="Sexo Biologico", max_length=9, choices=SEXO_BIOLOGICO)
    rg = models.CharField(verbose_name="RG", max_length=16, blank=True)
    cpf = models.CharField(verbose_name="CPF", max_length=14, default="86777069178")
    raca = models.CharField(verbose_name="Raça", max_length=9, choices=RACA)
    estado_civil = models.CharField(verbose_name="Estado Civil", max_length=10, choices=ESTADO_CIVIL)
    grau_instrucao = models.CharField(verbose_name="Grau de Instrução", max_length=200, choices=GRAU_INSTRUCAO)
    endereco = models.CharField(verbose_name="Endereço", max_length=200, default="Rua Antônio Barbosa Sobrinho")
    cep = models.CharField(verbose_name="CEP", max_length=9, default="39651970")
    bairro = models.CharField(verbose_name="Bairro", max_length=200, default="Centro")
    cidade = models.CharField(verbose_name="Cidade", max_length=200, default="Ribeirão da Folha")
    uf = models.CharField(verbose_name="UF", max_length=2, choices=UF_CHOICES)
    telefone_celular = models.CharField(verbose_name="Telefone Celular", max_length=11, default="33991514101")
    antecedentes_familiares = models.TextField(verbose_name="Antecedente Familiares",default="Dados de importância para a história clínica.")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Paciente Infantil"
        verbose_name_plural = "Pacientes Infantis"