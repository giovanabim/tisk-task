from django.db import models

from apps.usuarios.models import Usuario # para a chave estrangeira

class Lista(models.Model):
    NIVEIS_IMPORTANCIA = (
        ('muito_relevante', 'Muito Relevante'),
        ('intermedio', 'Intermédio'),
        ('nao_relevante', 'Não Relevante'),
    )

    nome = models.CharField(max_length=100)
    importancia = models.CharField(max_length=30, choices=NIVEIS_IMPORTANCIA, default='nao_relevante')
    # progresso = ?
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE) # mudei pare cascade pois nao irei manter o historio caso o user seja deletado

    def __str__(self):
        return f"{self.nome} - {self.importancia}" # tbm queria adicionar o progresso aq
