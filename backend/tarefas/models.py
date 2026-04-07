from django.db import models

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('ABERTA', 'Aberta'),
        ('EM_ANDAMENTO', 'Em Andamento'),
        ('CONCLUIDA', 'Concluída'),
        ('CANCELADA', 'Cancelada'),
        ('ATRASADA', 'Atrasada'),
    ]

    PRIORIDADE_CHOICES = [
        ('URGENTE', 'Urgente'),
        ('NAO_URGENTE', 'Não Urgente'),
    ]

    BUSCAR_CHOICES = [
        ('TITULO', 'Título'),
    ]

    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ABERTA')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_entrega = models.DateField()
    prioridade = models.CharField(max_length=20, choices=PRIORIDADE_CHOICES, default='NAO_URGENTE')
    buscar = models.CharField(max_length=20, choices=BUSCAR_CHOICES, default='TITULO')

    def __str__(self):
        return self.titulo