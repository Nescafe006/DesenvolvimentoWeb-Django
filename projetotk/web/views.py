from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from projetotask.models import tbl_usuarios
from projetotask.models import tbl_tarefas
from django.db.models import Sum
from web.forms import InsereTarefasForm, InsereUsuarioForm
from django.db.models import Count

class HomeView(TemplateView):
    template_name = "templates/_layouts/base.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()

        # Todas as tarefas
        context['tarefas'] = tbl_tarefas.objects.all()

        # Quantidade de tarefas por ID
        context['tarefas_usuario'] = tbl_tarefas.objects.values('id').annotate(
            numero_tarefas=Count('id'),
        )

        # Contagem total de tarefas
        context['total_tarefas'] = tbl_tarefas.objects.aggregate(total=Count("id"))

        # Contagem total de tarefas como quantidade
        context['qtde_tarefas'] = tbl_tarefas.objects.count()

        return context
    
  
        
        
class HomeUsuarioView(TemplateView):
    template_name = "web/usuarios/index.html"
    
    
class CriaUsuarioView(CreateView):
    template_name = "web/usuarios/cria.html"
    model = tbl_usuarios
    form_class =InsereUsuarioForm
    success_url = reverse_lazy("web:lista_Usuario")
    
    
class AtualizaUsuarioView(UpdateView):
    template_name = "web/usuarios/atualiza.html"
    model = tbl_tarefas
    fields = '__all__'
    context_object_name ='usuarios'
    success_url = reverse_lazy("web:lista_usuarios")
    
    
class DeletaUsuarioView(DeleteView):
    template_name ="web/usuarios/exclui.html"
    model = tbl_usuarios
    context_object_name = 'usuarios'
    success_url = reverse_lazy("web/lista_usuarios")
            
            
class ListaUsuarioView(ListView):
    template_name = "web/usuarios/lista.html"
    model = tbl_usuarios
    form_class = InsereUsuarioForm
    context_object_name = ("web:lista_usuarios")
    
#-------------------------------------------------------------------------------  
    
class HomeTarefasView(TemplateView):
    template_name = "web/tarefas/index.html"

class ListaTarefasView(ListView):
    template_name = "web/tarefas/lista.html"
    model = tbl_tarefas
    context_object_name = "tarefas"
    
class CriaTarefasView(CreateView):
    template_name ="web/tarefas/cria.html"
    model = tbl_tarefas
    form_class = InsereTarefasForm
    success_url = reverse_lazy("web/lista_tarefas")
    
class AtualizaTarefasView(UpdateView):
      template_name ="web/tarefas/atualiza.html"
      model = tbl_tarefas
      fields ='__all__'
      context_object_name = 'tarefas'
      success_url = reverse_lazy("web/lista_tarefas")
      
    
class DeletaTarefasView(DeleteView):
    template_name ="web/tarefas/exclui.html"
    model = tbl_tarefas
    context_object_name = 'tarefas'
    success_url = reverse_lazy("web/lista_tarefas")

#---------------------------------------------------------------------------
    
    
class HomeGerenciarView(TemplateView):
    template_name ="web/gerenciar/index.html"
    
class ListaTarefaView(ListView):
    template_name = "web/gerenciar/lista.html"
    model = tbl_tarefas
    context_object_name = "gerenciar"
    
class AtualizaTarefa(UpdateView):
    template_name = "web/gerenciar/atualiza.html"
    model = tbl_tarefas
    fields ='__all__'
    context_object_name = 'gerenciar'
    success_url = reverse_lazy("web:lista_tarefas")
    
class DeletaTarefa(UpdateView):
    template_name = "web/gerenciar/exclui.html"
    model = tbl_tarefas
    context_object_name = 'gerenciar'
    success_url = reverse_lazy("web:lista_tarefas")
