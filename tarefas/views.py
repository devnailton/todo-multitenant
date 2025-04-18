# tarefas/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Tarefa, Usuario
from django.contrib.auth.decorators import login_required # Para proteger views

# Exemplo de view simples baseada em função
@login_required # Garante que o usuário esteja logado
def home_tenant(request):
    # request.tenant contém o objeto Cliente (tenant) atual
    tenant_name = request.tenant.nome
    # request.user contém o objeto Usuario logado (do schema do tenant)
    user_name = request.user.username
    return HttpResponse(f"Bem-vindo à {tenant_name}, {user_name}! Esta é a home do tenant.")

# Exemplo usando ListView genérica para listar tarefas
class TarefaListView(ListView):
    model = Tarefa
    template_name = 'tarefas/tarefa_list.html' # Precisaremos criar este template
    context_object_name = 'tarefas' # Nome da variável no template

    def get_queryset(self):
        # Opcional: Filtrar tarefas, por exemplo, apenas as do usuário logado
        # return Tarefa.objects.filter(responsavel=self.request.user)
        return Tarefa.objects.all() # Por enquanto, lista todas do tenant

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tenant_name'] = self.request.tenant.nome # Passa o nome do tenant para o template
        return context

# Exemplo usando DetailView genérica para detalhes da tarefa
class TarefaDetailView(DetailView):
    model = Tarefa
    template_name = 'tarefas/tarefa_detail.html'
    context_object_name = 'tarefa'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tenant_name'] = self.request.tenant.nome
        return context

# --- Crie os Templates ---
# Crie a pasta 'templates/tarefas/' dentro do app 'tarefas'
# Crie os arquivos 'tarefa_list.html' e 'tarefa_detail.html' com conteúdo básico
# Exemplo 'tarefas/tarefa_list.html':
"""
<!DOCTYPE html>
<html>
<head><title>Tarefas - {{ tenant_name }}</title></head>
<body>
    <h1>Lista de Tarefas ({{ tenant_name }})</h1>
    {% if tarefas %}
        <ul>
            {% for tarefa in tarefas %}
                <li><a href="#">{{ tarefa.titulo }}</a> - {{ tarefa.get_status_display }}</li> {# Link para detail view #}
            {% endfor %}
        </ul>
    {% else %}
        <p>Nenhuma tarefa encontrada.</p>
    {% endif %}
    <p><a href="{% url 'admin:index' %}">Admin</a></p> {# Link para o admin do tenant #}
</body>
</html>
"""
# Adapte 'tarefa_detail.html' similarmente.