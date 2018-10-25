from django.urls import path

from curriculo import views

urlpatterns = [
    path('<str:sigla>/', views.curso, name="curso"),
<<<<<<< HEAD
    path('<str:sigladisc>/', views.disciplina, name="disciplina")
=======
    path('<str:sigla>/disciplina/<str:sigla_disciplina>/', views.disciplina, name="disciplina")
>>>>>>> kleber
]