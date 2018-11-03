# Generated by Django 2.1.1 on 2018-11-03 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, unique=True, verbose_name='Nome')),
                ('identificador', models.CharField(max_length=30, unique=True, verbose_name='Identificador')),
                ('data', models.DateField(auto_now_add=True, verbose_name='Data de Início')),
                ('status', models.CharField(choices=[('ABERTO', 'Aberta'), ('FECHADO', 'Fechada')], max_length=10, verbose_name='Status')),
                ('plano_de_ensino', models.TextField(blank=True, verbose_name='Plano de Ensino')),
                ('carga_horaria', models.SmallIntegerField(verbose_name='Carga Horária')),
                ('competencias', models.TextField(blank=True, verbose_name='Competências')),
                ('habilidades', models.TextField(blank=True, verbose_name='Habilidades')),
                ('ementa', models.TextField(blank=True, verbose_name='Ementa')),
                ('conteudo_programatico', models.TextField(blank=True, verbose_name='Conteúdo Programático')),
                ('bibliografia_basica', models.TextField(blank=True, verbose_name='Bibliografia Básica')),
                ('bibliografia_complementar', models.TextField(blank=True, verbose_name='Bibliografia Complementar')),
                ('percentual_pratico', models.SmallIntegerField(verbose_name='Percentual Prático')),
                ('percentual_teorico', models.SmallIntegerField(verbose_name='Percentual Teórico')),
            ],
            options={
                'db_table': 'DISCIPLINA',
            },
        ),
        migrations.CreateModel(
            name='DisciplinaOfertada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.SmallIntegerField(verbose_name='Ano')),
                ('semestre', models.SmallIntegerField(choices=[(1, '1º Semestre'), (2, '2º Semestre')], verbose_name='Semestre')),
                ('turma', models.CharField(max_length=1, verbose_name='Turma')),
                ('data_inicio', models.DateField(verbose_name='Data Ínicio')),
                ('data_fim', models.DateField(verbose_name='Data Fim')),
                ('metodologia', models.TextField(blank=True, verbose_name='Metodologia')),
                ('recursos', models.TextField(blank=True, verbose_name='Recursos')),
                ('criterio_de_avaliacao', models.TextField(blank=True, verbose_name='Critério de Avaliação')),
                ('plano_de_aulas', models.TextField(blank=True, verbose_name='Plano de Aulas')),
            ],
            options={
                'db_table': 'DISCIPLINA_OFERTADA',
            },
        ),
        migrations.AddField(
            model_name='curso',
            name='diurno',
            field=models.BooleanField(default=False, verbose_name='Diurno?'),
        ),
        migrations.AddField(
            model_name='curso',
            name='duracao',
            field=models.SmallIntegerField(default=4, verbose_name='Semestres'),
        ),
        migrations.AddField(
            model_name='curso',
            name='noturno',
            field=models.BooleanField(default=True, verbose_name='Noturno?'),
        ),
        migrations.AddField(
            model_name='curso',
            name='sobre',
            field=models.TextField(null=True, verbose_name='Sobre o curso'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='sigla',
            field=models.CharField(max_length=5, unique=True, verbose_name='Sigla'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='tipo',
            field=models.CharField(choices=[('T', 'Tecnólogo'), ('G', 'Graduação')], max_length=1, verbose_name='Tipo'),
        ),
        migrations.AddField(
            model_name='disciplinaofertada',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='curriculo.Curso'),
        ),
        migrations.AddField(
            model_name='disciplinaofertada',
            name='disciplina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='curriculo.Disciplina'),
        ),
    ]
