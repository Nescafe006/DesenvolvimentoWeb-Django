from django.urls import path
from web import views

app_name = 'web'

urlpatterns = [
    # ----------------------------------------- Home Views ----------------------------------------
    path('', views.home_view, name="index"),

    # ---------------------------------------- Usuários Views -------------------------------------
    path('usuarios/', views.home_usuario_view, name="index_usuarios"),
    path('usuarios/cadastrar', views.cria_usuario_view, name="cadastra_usuarios"),
    path('usuarios/lista', views.lista_usuario_view, name="lista_usuarios"),
    path('usuarios/<int:pk>', views.atualiza_usuario_view, name="atualiza_usuarios"),
    path('usuarios/excluir/<int:pk>', views.deleta_usuario_view, name="deleta_usuarios"),

    # ----------------------------------------- Tarefas Views ------------------------------------
    path('tarefas/', views.home_tarefas_view, name="index_tarefas"),
    path('tarefas/cadastrar', views.cria_tarefas_view, name="cadastra_tarefas"),
    path('tarefas/lista', views.lista_tarefas_view, name="lista_tarefas"),
    path('tarefas/<int:pk>', views.atualiza_tarefas_view, name="atualiza_tarefas"),
    path('tarefas/excluir/<int:pk>', views.deleta_tarefas_view, name="deleta_tarefas"),

    # --------------------------------------- Gerenciar Tarefas Views ---------------------------
    path('gerenciar/', views.home_gerenciar_view, name="index_gerenciar_tarefas"),
    path('gerenciar/lista', views.lista_tarefa_view, name="lista_tarefa"),
    path('gerenciar/<int:pk>', views.atualiza_tarefa_view, name="atualiza_tarefa"),
    path('gerenciar/excluir/<int:pk>', views.deleta_tarefa_view, name="deleta_tarefa"),
]

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
