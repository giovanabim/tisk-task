from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    senha = models.CharField(max_length=128) # nada seguro

    def __str__(self):
        return f"{self.nome} - {self.email}"
    