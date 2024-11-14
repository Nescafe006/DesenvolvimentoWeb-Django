from projetotask.models import tbl_usuarios, tbl_tarefas
from django import forms

class InsereUsuarioForm(forms.ModelForm):
    
    nome = forms.CharField(max_length=100, label=''
        
    )
    
    email = forms.EmailField(label='')
    
    
class meta:
    
    model = tbl_usuarios
    
    fields = [
        'usu_nome',
        'usu_email'
    ]
#------------------------------------------

class InsereTarefasForm(forms.ModelForm):
    class meta:
        
        model = tbl_tarefas
        
        fields = [
            'tar_descricao',
            'tar_setor',
            'tar_prioridade'
]