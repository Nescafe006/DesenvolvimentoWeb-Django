from django.forms import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from Sistemav1.models import Usuario
from django.views.generic import ListView, UpdateView, DeleteView, CreateView


def lista_usuario(request):
    # Primeiro, buscamos os funcionarios
    usuarios = Usuario.objetos.all()
    # Incluímos no contexto
    contexto = {'usuario': usuarios}
    # Retornamos o template para listar os funcionários
    return render(request, "templates/Usuario.html", contexto)

class ListaUsuario(ListView):
    template_name = "templates/usuario.html"
    model = Usuario
    context_object_name = "usuarios"

def cria_usuario(request, pk, form=None):

    # Verificamos se o método POST
    if request.method == 'POST':
        form = FormularioDeCriacao(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lista_usuarios'))
    # Qualquer outro método: GET, OPTION, DELETE, etc...
    else:
        return render(request, "templates/form.html", {'form': form})

class UsuarioListView(ListView):
    template_name = "web/lista.html"
model = Usuario
context_object_name = "usuario"


class UsuarioUpdateView(UpdateView):
    template_name = 'atualiza.html'
    model = Usuario
    fields = [
        'nome',
        'sobrenome',
        'cpf',
        'tempo_de_servico',
        'remuneracao'
    ]
    context_object_name = 'funcionario'

    def get_object(self, queryset=None):
        usuario = None

        # Os campos {pk} e {slug} estão presentes em self.kwargs
        id = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)

        if id is not None:
            # Busca o funcionario a partir do id
            usuario = Usuario.objects.filter(id=id).first()


        return usuario

    class UsuarioDeleteView(DeleteView):
        template_name = "website/exclui.html"

    model = Usuario
    context_object_name = 'usuario'
    success_url = reverse_lazy(
        "web:lista_usuario"
    )


    class UsuarioCreateView(CreateView):
        template_name = "website/cria.html"

    model = Usuario
    form_class = InsereUsuarioForm
    success_url = reverse_lazy("web:lista_Usuario")

    class InsereUsuarioForm(forms.Form):
        nome = forms.CharField(
            required=True,
            max_length=255
        )

        nome_usuario = forms.CharField(
            required=True,
            max_length=255
        )

        senha = forms.CharField(
            required=True,
            max_length=14
        )
