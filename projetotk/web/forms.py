from django import forms
from projetotask.models import *

class InsereUsuarioForm(forms.ModelForm):
    class Meta:
        model = tbl_usuarios
        fields = [
            'usu_nome',
            'usu_email'
        ]
        exclude = []
        
        

class InsereTarefaForm(forms.ModelForm):
    # Opções para o campo de prioridade
    Opcoes = [
        ('Baixa', 'Baixa'),
        ('Media', 'Média'),
        ('Alta', 'Alta'),
    ]
    

    Op = [
        ('Pendente', 'Pendente'),
        ('Concluída', 'Concluída'),
    ]

    tar_prioridade = forms.ChoiceField(choices=Opcoes, widget=forms.Select(attrs={'class': 'form-control'}))
    usuario = forms.ModelChoiceField(queryset=tbl_usuarios.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    tar_status = forms.ChoiceField(choices=Op, widget=forms.Select(attrs={'class': 'form-control'}))
    tar_descricao = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    tar_setor = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    tar_data = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}))

    
    class Meta:
        model = tbl_tarefas
        fields = ['tar_descricao', 'tar_setor', 'tar_prioridade', 'usuario', 'tar_data', 'tar_status']
        widgets = {
            'tar_descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'tar_setor': forms.TextInput(attrs={'class': 'form-control'}),
            'tar_data': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }