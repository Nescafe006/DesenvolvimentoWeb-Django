"""
URL configuration for Sistemav1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
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
from django.views import UsuarioListView
from django.views import UsuarioUpdateView
from django.views import UsuarioDeleteView
from django.views import UsuarioCreateView
urlpatterns = [
# Inclui as URLs do app website
path('', include('web.urls', namespace='web')),
# Interface administrativa
path('admin/', admin.site.urls),

path('usuarios/', UsuarioListView.as_view(), name='lista_usuarios'),

path(
'usuario/<id>',
UsuarioUpdateView.as_view(),
name='atualiza_usuario'),

path(
'usuario/excluir/<pk>',
UsuarioDeleteView.as_view(),
name='deleta_usuario'),

path(
'usuario/cadastrar/',
UsuarioCreateView.as_view(),
name='cadastra_usuario')

]

