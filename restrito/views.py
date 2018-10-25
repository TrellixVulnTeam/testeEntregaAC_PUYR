from django.shortcuts import render

def aluno(request):
    context = {}
    turmas = {
        "curso": {"nome":"Análise e Desenvolvimento de Sistemas", "semestre":"2","turma":"D"} 
    }

    mensagens = {
        "1": "Nota da prova incluída",
        "2": "AC Atribuida",
        "3": "AC Corrigida",
    }
    context = {
        "turmas": turmas['curso'],
        "mesagens": mensagens
    }
    
    return render(request, "restrito/aluno.html", context)