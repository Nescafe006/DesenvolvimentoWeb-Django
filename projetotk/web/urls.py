from django.contrib import admin
from django.urls import include, path
from web import views


app_name = 'web'


urlpatterns = [
    path('index/', views.index, name='index'),
    
    path('', views.logar, name='logar'),
    
    path('cadastro/', views.cadastro, name='cadastro'),


    path('usuarios/', views.UsuarioListView.as_view(), name='lista_usuarios'),

    path('usuario/cadastrar', views.UsuarioCreateView.as_view(), name='cadastra_usuario'),

    path('usuario/<int:pk>', views.UsuarioUpdateView.as_view(), name='atualiza_usuario'),

    path('usuario/excluir/<int:pk>', views.UsuarioDeleteView.as_view(), name='deleta_usuario'),


    path('tarefas/', views.TarefaListView.as_view(), name='lista_tarefas'),

    path('tarefa/cadastrar', views.TarefaCreateView.as_view(), name='cadastra_tarefa'),

    path('tarefa/excluir/<int:pk>', views.TarefaDeleteView.as_view(), name='deleta_tarefa'),

    path('atualiza_status/<int:pk>/', views.atualiza_status, name='atualiza_status'),
]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
