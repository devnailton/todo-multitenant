# clientes/urls.py
# Geralmente vazio ou com URLs específicas de gerenciamento de clientes
# que não ficam na raiz pública.
from django.urls import path
from . import views

app_name = 'clientes' # Boa prática adicionar namespace

urlpatterns = [
    # Exemplo: path('signup/', views.tenant_signup, name='signup'),
]