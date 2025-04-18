# app/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin do Django (acessível DENTRO de cada tenant)
    # Ex: http://clinica1.localhost:8000/admin/
    path('admin/', admin.site.urls),

    # Incluir as URLs do app 'tarefas' na raiz do tenant
    # Ex: http://clinica1.localhost:8000/ vai para tarefas.urls
    path('', include('tarefas.urls', namespace='tarefas')),
]