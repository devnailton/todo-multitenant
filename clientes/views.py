# clientes/views.py
from django.http import HttpResponse

def public_home(request):
    # Uma view simples para a raiz do domínio público (se houver)
    return HttpResponse("Página Pública Principal - Gerenciamento de Tenants (Exemplo)")

# Você adicionaria views para signup de novas clínicas aqui, por exemplo.