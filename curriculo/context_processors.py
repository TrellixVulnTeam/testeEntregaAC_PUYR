

def lista_cursos(request):
    return {
        "cursos":[
            {"nome":"Sistemas da Informação", "sigla":"SI"},
            {"nome":"Análise e Desenvolvimento de Sistemas", "sigla":"ADS"},
            {"nome":"Banco de Dados", "sigla":"BD"}
        ]
    }