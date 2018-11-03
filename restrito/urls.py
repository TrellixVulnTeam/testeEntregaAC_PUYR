from django.urls import path

from restrito import views

app_name = "restrito"


urlpatterns = [
    path('aluno/', views.aluno, name="aluno"),
    path('professor/', views.professor, name="professor")
]