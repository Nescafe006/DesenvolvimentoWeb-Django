import self
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from projCadastro.models import Funcionario
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from django.http import HttpResponseRedirect
from projCadastro.forms import FormularioDeCriacao  # Certifique-se de importar seu formulário

def lista_funcionarios(request):
    # Primeiro, buscamos os funcionarios
    funcionarios = Funcionario.objects.all()  # Corrigido de objetos para objects
    # Incluímos no contexto
    contexto = {'funcionarios': funcionarios}
    # Retornamos o template para listar os funcionários
    return render(request, "funcionarios.html", contexto)  # Corrigido o caminho do template

class ListaFuncionarios(ListView):
    template_name = "funcionarios.html"  # Corrigido o caminho do template
    model = Funcionario
    context_object_name = "funcionarios"

def cria_funcionario(request, pk):
    # Verificamos se o método POST
    if request.method == 'POST':
        form = FormularioDeCriacao(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lista_funcionarios'))
    else:
        form = FormularioDeCriacao()  # Cria um formulário vazio para requisições GET
    return render(request, "form.html", {'form': form})  # Corrigido o caminho do template

class FuncionarioListView(ListView):

    template_name = "website/lista.html"
    model = Funcionario
    context_object_name = "funcionarios"

    class FuncionarioUpdateView(UpdateView):
        template_name = 'atualiza.html'

    model = Funcionario
    fields = fields = [
        'nome',
        'sobrenome',
        'cpf',
        'tempo_de_servico',
        'remuneracao'
        ]
    context_object_name = 'funcionario'

    def get_object(self, queryset=None):
        funcionario = None

        # Get the primary key and slug from kwargs
        id = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)

        if id is not None:
            funcionario = Funcionario.objects.filter(id=id).first()

        return funcionario


    class FuncionarioDeleteView(DeleteView):
        template_name = "website/exclui.html"
        model = Funcionario
        context_object_name = 'funcionario'
        success_url = reverse_lazy("website:lista_funcionarios")

        def get_object(self, queryset=None):

            # Get the primary key and slug from kwargs
            id = self.kwargs.get(self.pk_url_kwarg)
            slug = self.kwargs.get(self.slug_url_kwarg)

            # First, try to find the object by id
            if id is not None:
                funcionario = queryset.filter(id=id).first()

            # If not found by id, try to find by slug

                funcionario = queryset.filter(**{self.slug_url_kwarg: slug}).first()

                return funcionario


class FuncionarioCreateView(CreateView):
    template_name = "website/cria.html"
    model = Funcionario
    form_class = InsereFuncionarioForm
    success_url = reverse_lazy("website:lista_funcionarios")