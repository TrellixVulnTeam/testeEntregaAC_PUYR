from django.db import models

# Create your models here.
class Curso(models.Model):
    TIPOS = (
        ('TECNICO','Técnico'),
        ('GRADUACAO','Graduação'),
        ('PGRADUACAO','Pós-Graduação')
    )
    nome = models.CharField('Nome', max_length=120)
    sigla = models.CharField('Sigla',max_length=10,unique=True)
    tipo = models.CharField(
        "Tipo de Curso"
        ,max_length=20
        ,choices=TIPOS
    )

    class Meta:
        db_table = 'CURSO'

    def __str__(self):
        return self.nome
