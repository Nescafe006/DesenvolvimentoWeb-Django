from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import  render
from django.urls import reverse, reverse_lazy
from projetotask.models import *
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import CreateView
from web.forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# HomeView
def index(request):
    return render(request, 'index.html')

def logar(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(request, username=username, password=senha)
        
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('web:index'))
        else:
            messages.error(request,'Usuário e/ou senha estão incorretos.')

    return render(request, 'login.html')
        
def cadastro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            messages.error(request,'Usuário já existe.')
        else:
            user = User.objects.create_user(username=username, password=senha)
            user.save()
            return HttpResponseRedirect(reverse('web:logar'))
        
    return render(request, 'cadastro.html')


   
# HomeUsuarioView
class UsuarioListView(LoginRequiredMixin, ListView):
    template_name = 'lista_usuarios.html'
    model = tbl_usuarios
    context_object_name = 'usuarios'

class UsuarioCreateView(LoginRequiredMixin, CreateView):
    template_name = 'cadastra_usuario.html'
    model = tbl_usuarios
    form_class = InsereUsuarioForm
    success_url = reverse_lazy('web:lista_usuarios') 

class UsuarioUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'atualiza.html'
    model = tbl_usuarios
    fields = ['usu_nome', 'usu_email']
    context_object_name = 'usuarios'

    def get_success_url(self):
        return reverse_lazy('web:lista_usuarios')
    
    
    def get_object(self):
        usuario = None

        id = self.kwargs.get(self.pk_url_kwarg)
        if id is not None:
            usuario = tbl_usuarios.objects.filter(usu_codigo=id).first()
        return usuario
    
    success_url = reverse_lazy('web:lista_usuarios')

class UsuarioDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'exclui_usuario.html'
    model = tbl_usuarios
    context_object_name = 'usuarios'
    success_url = reverse_lazy('web:lista_usuarios')


class TarefaListView(LoginRequiredMixin,ListView):
    template_name = 'lista_tarefas.html'
    model = tbl_tarefas
    context_object_name = 'tarefas'

class TarefaCreateView(LoginRequiredMixin,CreateView):
    template_name = 'cadastra_tarefa.html'
    model = tbl_tarefas
    form_class = InsereTarefaForm
    success_url = reverse_lazy('web:lista_tarefas')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class TarefaDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'exclui_tarefa.html'
    model = tbl_tarefas
    context_object_name = 'tarefas'  
    success_url = reverse_lazy('web:lista_tarefas')

    
    
def atualiza_status(request, pk):
    if request.method == 'POST':
        novo_status = request.POST.get('novo_status')
      
        if novo_status not in ['Pendente', 'Concluída']:
            messages.error(request, 'Status inválido.')
            return HttpResponseRedirect(reverse('web:lista_tarefas'))

        tarefa = tbl_tarefas.objects.filter(tar_codigo=pk).first()

        if tarefa:
            tarefa.tar_status = novo_status  
            tarefa.save()
            messages.success(request, 'Status atualizado com sucesso!')
        else:
            messages.error(request, 'Tarefa não encontrada.')

        return HttpResponseRedirect(reverse('web:lista_tarefas'))

