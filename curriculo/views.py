from django.shortcuts import render

def curso(request, sigla):
    cursos = {
        "SI": {"nome":"Sistemas da Informação", "sigla":"SI","disciplina":"BD"},
        "ADS": {"nome":"Análise e Desenvolvimento de Sistemas", "sigla":"ADS"},
        "BD": {"nome":"Banco de Dados", "sigla":"BD"}
    }
    context = {
        "atual": cursos[sigla]
    }
    return render(request, "curriculo/curso.html", context)

def disciplina(request,sigladisc):
    disciplinas = {
        "SI": {"nome":"Fundamentos de Banco de Dados", "descricao":"BD","ementa":""},
        "ADS": {"nome":"Linguagem de programação 1", "sigla":"LP1"},
        "BD": {"nome":"Introdução a Internet das Coisas", "sigla":"IOT"}
    }
    context = {
        "atual": disciplinas[sigladisc]
    }
    return render(request, "curriculo/disciplina.html", context)