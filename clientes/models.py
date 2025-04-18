# clientes/models.py
from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

class Cliente(TenantMixin):
    nome = models.CharField("Nome da Clínica", max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)
    # auto_create_schema = True # Mantenha comentado por enquanto

    def __str__(self):
        return self.nome

class Dominio(DomainMixin):
    def __str__(self):
        return self.domain