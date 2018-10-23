from django.urls import path

from curriculo import views

urlpatterns = [
    path('<str:sigla>/', views.curso, name="curso")
]