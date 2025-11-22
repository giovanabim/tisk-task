from django.db import models

from apps.usuarios.models import Usuario # para a chave estrangeira de usuarios
from apps.listas.models import Lista # para a chave estrangeira de listas

class Tag(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    nome = models.CharField(max_length=100)
    concluido = models.BooleanField(default=False)
    prazo = models.DateField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE) # mudei pare cascade pois nao irei manter o historio caso o user seja deletado
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.concluido} - {self.prazo} - {self.tags}"
    