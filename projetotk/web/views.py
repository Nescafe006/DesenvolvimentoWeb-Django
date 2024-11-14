from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from projetotk.models import tbl_usuario
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from projetotask.models import tbl_usuario
from projetotask.models import tbl_tarefas

def my_view(request):
    my_objects = tbl_usuario.objects.all()
    my_objects = tbl_tarefas.objects.all()
    

    return render(request, 'web/templates.html',{'my_objects': my_objects})


def cria_usuario(request, pk):
    
    if request.method =='POST':
        form = FormularioDeCriacao(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lista_funcionario'))
        else:
            form = FormularioDeCriacao()
            return render(request, "form.html", {'form': form})
        
class UsuarioListView(Listview):

    template_name = "web/lista.html"
    model = tbl_usuario
    context_object_name ="usuarios"

    class UsuarioUpdateView(Updateview):
        template_name = 'atualiza.html'

    model = tbl_usuario
    fields = fields = [
        'nome',
        'email',
    ]
    context_object_name = 'usuario'

    def get_object(self, queryset=None):
        usuario = None

          # Get the primary key and slug from kwargs
        id = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)


        if id is not None:
            usuario = tbl_usuario.objects.filter(id=id).first()
            return usuario
        

    class UsuarioDeleteView(DeleteView):
        template_name = "web/exclui.html"
        model = tbl_usuario
        context_object_name ='usuario'
        sucess_url = reverse_lazy