from django.shortcuts import render,get_object_or_404
from curriculo.models import Curso, Disciplina, DisciplinaOfertada

def curso(request, sigla):
    curso = get_object_or_404(Curso, sigla=sigla)
    curso.semestres = [
        'Semestre 2',
    ]
    disciplinas = DisciplinaOfertada.objects.filter(ano=2018,semestre=2,curso=curso)

    context = {
        "curso": curso,
        "disciplinas_ofertadas": disciplinas
    }

    return render(request, "curriculo/curso.html", context)

def disciplina(request,sigla,sigla_disciplina):
    context = {}
    disciplina = Disciplina.objects.get(identicador=sigla_disciplina)
    context = {
        "disciplina": disciplina
    }

    return render(request, "curriculo/disciplina.html", context)
