# tarefas/urls.py
from django.urls import path
from . import views

app_name = 'tarefas' # Namespace

urlpatterns = [
    # Raiz do domínio do tenant (ex: http://clinica1.localhost:8000/)
    path('', views.home_tenant, name='home_tenant'),

    # URLs para as views genéricas de Tarefa
    path('tarefas/', views.TarefaListView.as_view(), name='tarefa_list'),
    path('tarefas/<int:pk>/', views.TarefaDetailView.as_view(), name='tarefa_detail'),

    # Adicione outras URLs aqui (criar tarefa, editar, etc.)
]