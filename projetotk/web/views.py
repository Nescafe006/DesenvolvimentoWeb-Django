from django.shortcuts import render
from projetotask.models import tbl_usuario
from projetotask.models import tbl_tarefas

def my_view(request):
    my_objects = tbl_usuario.objects.all()
    my_objects = tbl_tarefas.objects.all()
    

    return render(request, 'web/templates.html',{'my_objects': my_objects})

# Create your views here.
