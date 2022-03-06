# Generated by Django 4.0.3 on 2022-03-05 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome Disciplina')),
                ('codigo', models.CharField(max_length=200, verbose_name='CodDisc')),
                ('periodo', models.CharField(choices=[('1º', '1º'), ('2º', '2º'), ('3º', '3º'), ('4º', '4º'), ('5º', '5º'), ('6º', '6º'), ('7º', '7º'), ('8º', '8º'), ('9º', '9º'), ('10º', '10º')], max_length=3, verbose_name='Periodo')),
            ],
        ),
        migrations.CreateModel(
            name='Distribuicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_atendimento', models.DateTimeField(verbose_name='Data/Hora Atendimento')),
                ('procedimento', models.CharField(choices=[('restaurações', 'RESTAURAÇÃO'), ('aplicação de flúor', 'APLICAÇÃO FLUOR'), ('tratamentos de canal', 'TRATAMENTO CANAL'), ('tratamento de bruxismo', 'TRATAMENTO BRUXISMO')], max_length=200, verbose_name='Procedimento')),
            ],
        ),
    ]
