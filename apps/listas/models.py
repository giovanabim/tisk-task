from django.db import models

from apps.usuarios.models import Usuario # para a chave estrangeira

class Lista(models.Model):
    NIVEIS_PRIORIDADE = (
        ('alta', 'Alta'),
        ('media', 'Média'),
        ('baixa', 'Baixa'),
    )

    nome = models.CharField(max_length=100)
    prioridade = models.CharField(max_length=10, choices=NIVEIS_PRIORIDADE, default='baixa')
    # progresso = ?
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE) # mudei pare cascade pois nao irei manter o historio caso o user seja deletado

    def calcular_progresso(self):
        total_tarefas = self.tarefa_set.count() # Usa o nome 'tarefa_set' (relação inversa)
        if total_tarefas == 0:
            return 0
        
        tarefas_concluidas = self.tarefa_set.filter(concluido=True).count()
        return (tarefas_concluidas / total_tarefas) * 100

    def __str__(self):
        progresso = round(self.calcular_progresso())
        return f"{self.nome} - {self.prioridade} - {progresso}%" 
