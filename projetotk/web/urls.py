from django.urls import path
from web import views

app_name = 'web'

urlpatterns =[
    
    path('', views.HomeView.as_view(), name="index"),
    
    
    path('usuarios/', views.HomeUsuarioView.as_view(), name="index_usuarios"),

    path('usuarios/cadastrar', views.CriaUsuarioView.as_view(), name="cadastra_usuarios"),

    path('usuarios/lista', views.ListaUsuarioView.as_view(), name="lista_usuarios"),

    path('usuarios/<pk>', views.AtualizaUsuarioView.as_view(), name="atualiza_usuarios"),

    path('usuarios/excluir/<pk>', views.DeletaUsuarioView.as_view(), name="deleta_usuarios"),
#---------------------------------------------------------------------------------------------

  
    path('tarefas/', views.HomeTarefasView.as_view(), name="index_tarefas"),

    path('tarefas/cadastrar', views.CriaTarefasView.as_view(), name="cadastra_tarefas"),

    path('tarefas/lista', views.ListaTarefasView.as_view(), name="lista_tarefas"),

    path('tarefas/<pk>', views.AtualizaTarefasView.as_view(), name="atualiza_tarefas"),

    path('tarefas/excluir/<pk>', views.DeletaTarefasView.as_view(), name="deleta_tarefas"),
    
    #-----------------------------------------------------------------------------------------
    
 
    path('gerenciar/', views.HomeGerenciarView.as_view(), name="index_gerenciar_tarefas"),

    path('gerenciar/lista', views.ListaTarefaView.as_view(), name="lista_tarefa"),

    path('gerenciar/<pk>', views.AtualizaTarefa.as_view(), name="atualiza_tarefa"),

    path('gerenciar/excluir/<pk>', views.DeletaTarefa.as_view(), name="deleta_tarefa"),
]

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
