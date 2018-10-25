from django.urls import path

from curriculo import views

urlpatterns = [
    path('<str:sigla>/', views.curso, name="curso"),
    path('<str:sigla>/disciplina/<str:sigla_disciplina>/', views.disciplina, name="disciplina")
]