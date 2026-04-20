from django.db import models

class Usuarios(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.nome