from django.shortcuts import render, redirect
from django.http import HttpResponse
from projetotask.models import tbl_tarefas, tbl_usuarios
from django.db.models import Count
from django.urls import reverse_lazy
from .forms import InsereUsuarioForm, InsereTarefasForm

# HomeView
def home_view(request):
    tarefas = tbl_tarefas.objects.all()

    tarefas_usuario = tbl_tarefas.objects.values('id').annotate(
        numero_tarefas=Count('id'),
    )

    total_tarefas = tbl_tarefas.objects.aggregate(total=Count("id"))
    qtde_tarefas = tbl_tarefas.objects.count()

    context = {
        'tarefas': tarefas,
        'tarefas_usuario': tarefas_usuario,
        'total_tarefas': total_tarefas,
        'qtde_tarefas': qtde_tarefas
    }
    return render(request, "base.html", context)

# HomeUsuarioView
def home_usuario_view(request):
    return render(request, "templates/usuarios/index.html")

# CriaUsuarioView
def cria_usuario_view(request):
    if request.method == 'POST':
        form = InsereUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('web:lista_usuarios'))
    else:
        form = InsereUsuarioForm()

    return render(request, "usuarios/cria.html", {'form': form})

# AtualizaUsuarioView
def atualiza_usuario_view(request, pk):
    usuario = tbl_usuarios.objects.get(pk=pk)
    if request.method == 'POST':
        form = InsereUsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('web:lista_usuarios'))
    else:
        form = InsereUsuarioForm(instance=usuario)

    return render(request, "templates/usuarios/atualiza.html", {'form': form, 'usuario': usuario})

# DeletaUsuarioView
def deleta_usuario_view(request, pk):
    usuario = tbl_usuarios.objects.get(pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect(reverse_lazy('web:lista_usuarios'))

    return render(request, "templates/usuarios/exclui.html", {'usuario': usuario})

# ListaUsuarioView
def lista_usuario_view(request):
    usuarios = tbl_usuarios.objects.all()
    return render(request, "templates/usuarios/lista.html", {'usuarios': tbl_usuarios})

# HomeTarefasView
def home_tarefas_view(request):
    return render(request, "templates/tarefas/index.html")

# ListaTarefasView
def lista_tarefas_view(request):
    tarefas = tbl_tarefas.objects.all()
    return render(request, "templates/tarefas/lista.html", {'tarefas': tarefas})

# CriaTarefasView
def cria_tarefas_view(request):
    if request.method == 'POST':
        form = InsereTarefasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('web:lista_tarefas'))
    else:
        form = InsereTarefasForm()

    return render(request, "templates/tarefas/cria.html", {'form': form})

# AtualizaTarefasView
def atualiza_tarefas_view(request, pk):
    tarefa = tbl_tarefas.objects.get(pk=pk)
    if request.method == 'POST':
        form = InsereTarefasForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('web:lista_tarefas'))
    else:
        form = InsereTarefasForm(instance=tarefa)

    return render(request, "templates/tarefas/atualiza.html", {'form': form, 'tarefa': tarefa})

# DeletaTarefasView
def deleta_tarefas_view(request, pk):
    tarefa = tbl_tarefas.objects.get(pk=pk)
    if request.method == 'POST':
        tarefa.delete()
        return redirect(reverse_lazy('web:lista_tarefas'))

    return render(request, "templates/tarefas/exclui.html", {'tarefa': tarefa})

# HomeGerenciarView
def home_gerenciar_view(request):
    return render(request, "templates/gerenciar/index.html")

# ListaTarefaView (gerenciamento)
def lista_tarefa_view(request):
    tarefas = tbl_tarefas.objects.all()
    return render(request, "templates/gerenciar/lista.html", {'gerenciar': tarefas})

# AtualizaTarefa
def atualiza_tarefa_view(request, pk):
    tarefa = tbl_tarefas.objects.get(pk=pk)
    if request.method == 'POST':
        form = InsereTarefasForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('web:lista_tarefas'))
    else:
        form = InsereTarefasForm(instance=tarefa)

    return render(request, "templates/gerenciar/atualiza.html", {'form': form, 'gerenciar': tarefa})

# DeletaTarefa
def deleta_tarefa_view(request, pk):
    tarefa = tbl_tarefas.objects.get(pk=pk)
    if request.method == 'POST':
        tarefa.delete()
        return redirect(reverse_lazy('web:lista_tarefas'))

    return render(request, "templates/gerenciar/exclui.html", {'gerenciar': tarefa})
