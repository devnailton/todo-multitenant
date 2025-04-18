# app/urls_public.py
from django.urls import path, include
# Importe views do app clientes se quiser usá-las na raiz pública
from clientes import views as clientes_views

urlpatterns = [
    # Raiz do domínio público (ex: http://localhost:8000/)
    path('', clientes_views.public_home, name='public_home'),

    # Incluir URLs específicas do app clientes (se houver)
    # path('clientes/', include('clientes.urls', namespace='clientes')),

    # NÃO inclua admin.site.urls aqui, pois admin/auth estão em TENANT_APPS
]