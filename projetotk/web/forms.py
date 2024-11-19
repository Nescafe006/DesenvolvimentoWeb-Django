from projetotask.models import tbl_usuarios, tbl_tarefas
from django import forms

class InsereUsuarioForm(forms.ModelForm):
    class Meta:  # "Meta" com M maiúsculo
        model = tbl_usuarios  # Associa ao modelo correto
        fields = ['usu_nome', 'usu_email']  # Campos que o formulário deve manipular
        labels = {
            'usu_nome': 'Nome do Usuário',
            'usu_email': 'E-mail',
        }

class InsereTarefasForm(forms.ModelForm):
    class Meta:  # "Meta" com M maiúsculo
        model = tbl_tarefas  # Associa ao modelo correto
        fields = ['tar_descricao', 'tar_setor', 'tar_prioridade']  # Campos do modelo
        labels = {
            'tar_descricao': 'Descrição',
            'tar_setor': 'Setor',
            'tar_prioridade': 'Prioridade',
        }
