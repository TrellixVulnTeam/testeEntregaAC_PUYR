from django.shortcuts import render

def curso(request, sigla):
    cursos = {
<<<<<<< HEAD
        "SI": {"nome":"Sistemas da Informação", "sigla":"SI","disciplina":"BD"},
        "ADS": {"nome":"Análise e Desenvolvimento de Sistemas", "sigla":"ADS"},
        "BD": {"nome":"Banco de Dados", "sigla":"BD"}
=======
        "SI": {"nome":"Sistemas da Informação"
             , "sigla":"SI"
             , "descricao":"A Graduação de Sistemas de Informação prepara o aluno para ser um profissional transformador do mercado, desenvolvendo soluções inovadoras e criativas na construção e utilização de Sistemas de Informação."
             , "coordenador": "Osvaldo Kotaro Takai"
             , "grade": {"semestre":"1","disciplina": "Comunicação e Expressão (EAD)","sigla_disciplina":"CE"}},
        "ADS": {"nome":"Análise e Desenvolvimento de Sistemas"
             , "sigla":"ADS"
             , "descricao":"A Graduação de Sistemas de Informação prepara o aluno para ser um profissional transformador do mercado, desenvolvendo soluções inovadoras e criativas na construção e utilização de Sistemas de Informação."
             , "coordenador": "Ana Cristina dos Santos"
             , "grade": {"semestre":"2","disciplina": "Tecnologia WEB","sigla_disciplina":"TecWeb"}},
        "BD": {"nome":"Banco de Dados", "sigla":"BD"
               , "descricao":"A Graduação de Sistemas de Informação prepara o aluno para ser um profissional transformador do mercado, desenvolvendo soluções inovadoras e criativas na construção e utilização de Sistemas de Informação."
             , "coordenador": "Osvaldo Kotaro Takai"
             , "grade": {"semestre":"1","disciplina": "Fundamentos de Banco de Dados","sigla_disciplina":"FBD"}},
>>>>>>> kleber
    }

    context = {
        "atual": cursos[sigla]
    }
    return render(request, "curriculo/curso.html", context)

<<<<<<< HEAD
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
=======
def disciplina(request,sigla,sigla_disciplina):
    context = {}
    disciplinas = {
        "CE": {"nome":"Comunicação e Expressão (EAD)", "sigla_disciplina":"CE","descricao":"A fluência na língua materna possibilita a plena compreensão dos textos indicados e a excelência na produção cientifica. Aplicação prática da expressividade ao falar em público, com direcionamento acadêmico e empresarial. Desenvolvimento de textos corporativos e científicos. Leitura crítica e interpretativa. Elaboração de textos, permeados pela clareza, intencionalidade, coesão e coerência. Orientação para emprego da ABNT em produções científicas."},
        "TecWeb": {"nome":"Tecnologia WEB", "sigla_disciplina":"TecWeb","descricao":"Conceitos e fundamentos: Internet, Intranet e Extranet. Arquitetura Cliente-Servidor. Desenvolvimento de aplicações WEB Padrões Web. HTML (HyperText Markup Language) e CSS ( Cascading Style Sheets). Sintaxe, comandos JavaScript e integração com HTML. Noções de NodeJS. Python e Framework de Desenvolvimento.  Arquitetura Model-View-Controller; a camada de acesso a banco de dados; Padrão de endereçamento http; aspetos de segurança, componentização JQuery + AJAX."},
        "FBD": {"nome":"Fundamento BD", "sigla_disciplina":"FBD","descricao":"A fluência na língua materna possibilita a plena compreensão dos textos indicados e a excelência na produção cientifica. Aplicação prática da expressividade ao falar em público, com direcionamento acadêmico e empresarial. Desenvolvimento de textos corporativos e científicos. Leitura crítica e interpretativa. Elaboração de textos, permeados pela clareza, intencionalidade, coesão e coerência. Orientação para emprego da ABNT em produções científicas."}
    }
    context = {
        "disciplina_data": disciplinas[sigla_disciplina]
    }
    return render(request, "curriculo/disciplina.html", context)
>>>>>>> kleber
