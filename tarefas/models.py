# tarefas/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings # Importar settings

class Usuario(AbstractUser):
    NIVEL_ACESSO_CHOICES = [
        ('owner', 'Owner'),
        ('admin', 'Administrator'),
        ('leader', 'Leader'),
        ('operational', 'Operational'),
    ]
    nivel_acesso = models.CharField(
        max_length=20,
        choices=NIVEL_ACESSO_CHOICES,
        default='operational'
    )
    # Não precisa de campo clínica aqui

    def __str__(self):
        return f"{self.username} ({self.get_nivel_acesso_display()})"

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('andamento', 'Em andamento'),
        ('concluida', 'Concluída'),
    ]
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_conclusao = models.DateTimeField(null=True, blank=True)
    # Usar settings.AUTH_USER_MODEL é a forma mais robusta
    responsavel = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True, # Permitir tarefas sem responsável inicial
        related_name='tarefas'
    )

    def __str__(self):
        return self.titulo