from django.db import models
from datetime import date, datetime


class Curso(models.Model):

    TIPOS_CURSOS = (
        ('T', 'Tecnólogo'),
        ('G', 'Graduação')
    )
    nome = models.CharField('Nome', max_length=120)

    sigla = models.CharField('Sigla', max_length=5, unique=True)

    sobre = models.TextField('Sobre o curso', null=True)

    duracao = models.SmallIntegerField('Semestres',default=4)

    tipo = models.CharField('Tipo', max_length=1, choices=TIPOS_CURSOS)

    noturno = models.BooleanField('Noturno?',default=True)

    diurno = models.BooleanField('Diurno?',default=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'CURSO'



class Disciplina(models.Model):
    STATUS = (
        ('ABERTO','Aberta'),
        ('FECHADO', 'Fechada')
    )
    nome = models.CharField(
        'Nome',
        max_length=30,
        unique=True
    )

    identificador = models.CharField(
        'Sigla',
        max_length=30,
        unique=True
    )

    data = models.DateField(
        "Data de Início",
        auto_now_add=True
    )

    status = models.CharField(
        "Status",
        max_length=10,
        choices=STATUS
    )

    plano_de_ensino = models.TextField(
        "Plano de Ensino",
        blank=True
    )

    carga_horaria = models.SmallIntegerField(
        "Carga Horária"
    )

    competencias = models.TextField(
        "Competências",
        blank=True
    )

    habilidades = models.TextField(
        "Habilidades",
        blank=True
    )

    ementa = models.TextField(
        "Ementa",
        blank=True
    )


    conteudo_programatico = models.TextField(
        "Conteúdo Programático",
        blank=True
    )

    bibliografia_basica = models.TextField(
        "Bibliografia Básica",
        blank=True
    )

    bibliografia_complementar = models.TextField(
        "Bibliografia Complementar",
        blank=True
    )

    percentual_pratico = models.SmallIntegerField(
        "Percentual Prático"
    )

    percentual_teorico = models.SmallIntegerField(
        "Percentual Teórico"
    )
    

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'DISCIPLINA'


class DisciplinaOfertada(models.Model):
    SEMESTRES = (
        (1, '1º Semestre'),
        (2, '2º Semestre')
    )
    curso = models.ForeignKey(
        'curriculo.Curso',
        on_delete=models.DO_NOTHING
    )

    disciplina = models.ForeignKey(
        'curriculo.Disciplina',
        on_delete=models.DO_NOTHING
    )

    ano = models.SmallIntegerField('Ano')

    semestre = models.SmallIntegerField(
        'Semestre',
        choices=SEMESTRES
    )

    turma = models.CharField('Turma', max_length=1)

    data_inicio = models.DateField(
        "Data Ínicio"
    )

    data_fim = models.DateField("Data Fim")

    metodologia = models.TextField("Metodologia", blank=True)

    recursos = models.TextField("Recursos", blank=True)

    criterio_de_avaliacao = models.TextField("Critério de Avaliação", blank=True)

    plano_de_aulas = models.TextField("Plano de Aulas", blank=True)

    class Meta:
        db_table = 'DISCIPLINA_OFERTADA'