from django.shortcuts import render

def curso(request, sigla):
    cursos = {
        "SI": {"nome":"Sistemas da Informação", "sigla":"SI"},
        "ADS": {"nome":"Análise e Desenvolvimento de Sistemas", "sigla":"ADS"},
        "BD": {"nome":"Banco de Dados", "sigla":"BD"}
    }
    context = {
        "atual": cursos[sigla]
    }
    return render(request, "curriculo/curso.html", context)