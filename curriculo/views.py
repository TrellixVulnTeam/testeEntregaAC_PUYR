from django.shortcuts import render,get_object_or_404
from curriculo.models import Curso, Disciplina, DisciplinaOfertada
from datetime import datetime

def curso(request, sigla):
    curso = get_object_or_404(Curso, sigla=sigla)
    curso.semestres = [
        'Semestre 2',
    ]
    ano = datetime.now().year
    sem_corrente = 1 if datetime.now().month <=6 else 2
    disciplinas = DisciplinaOfertada.objects.filter(ano=ano,semestre=sem_corrente,curso=curso)

    context = {
        "curso": curso,
        "disciplinas_ofertadas": disciplinas
    }

    return render(request, "curriculo/curso.html", context)

def disciplina(request,sigla,sigla_disciplina):
    context = {}
    disciplina = Disciplina.objects.get(identificador=sigla_disciplina)
    context = {
        "disciplina": disciplina
    }

    return render(request, "curriculo/disciplina.html", context)
