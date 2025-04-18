# tarefas/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin # Renomear para evitar conflito
from .models import Usuario, Tarefa

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status', 'responsavel', 'data_criacao', 'data_conclusao')
    list_filter = ('status', 'responsavel', 'data_criacao')
    search_fields = ('titulo', 'descricao')
    date_hierarchy = 'data_criacao'

# Customizar o Admin para o nosso Usuario customizado
class UsuarioAdmin(BaseUserAdmin):
    # Adicionar 'nivel_acesso' aos fieldsets existentes
    # Copiar fieldsets do BaseUserAdmin e adicionar o seu campo
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Nível de Acesso', {'fields': ('nivel_acesso',)}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {'fields': ('nivel_acesso',)}),
    )
    list_display = BaseUserAdmin.list_display + ('nivel_acesso',) # Adicionar à lista

# Registrar Usuario com o admin customizado
admin.site.register(Usuario, UsuarioAdmin)