"""
URL configuration for projCadastro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views. Home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls.conf import include
from django.contrib import admin
from django.urls import path
from website import views
from projCadastro.views import FuncionarioCreateView

# urlpatterns contém a lista de roteamentos de URLs
urlpatterns = [
    #inclui as urls do app website'
    path('', include('website.urls', namespace='website')),
    #interface administrativa
    path('admin/', admin.site.urls),

path('funcionarios/', FuncionarioListView.as_view(), name='lista_funcionarios'),

path(
'funcionario/<id>',
FuncionarioUpdateView.as_view(),
name='atualiza_funcionario'),

path(
'funcionario/excluir/<pk>',
FuncionarioDeleteView.as_view(),
name='deleta_funcionario'),


path(
'funcionario/cadastrar/',
FuncionarioCreateView.as_view(),
name='cadastra_funcionario'),


]




