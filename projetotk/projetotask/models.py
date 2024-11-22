from django.db import models
from django.contrib.auth.models import User

class tbl_usuarios(models.Model):
    usu_codigo = models.AutoField(primary_key=True)
    usu_nome = models.CharField(max_length=255, db_column='usu_nome')
    usu_email = models.EmailField(max_length=255, db_column='usu_email')

    def __str__(self):
        return self.usu_nome

    class Meta:
        db_table = 'tbl_usuarios'



class tbl_tarefas(models.Model):
    tar_codigo = models.AutoField(primary_key=True)
    tar_descricao = models.CharField(max_length=255, db_column='tar_descricao')
    tar_setor = models.CharField(max_length=100, db_column='tar_setor')
    tar_prioridade = models.CharField(max_length=5, choices=[('Baixa', 'Baixa'), ('Media', 'Média'), ('Alta', 'Alta')])
    tar_data = models.DateField()
    tar_status = models.CharField(max_length=20, choices=[('Pendente', 'Pendente'), ('Concluída', 'Concluída')])
    
    # Definindo corretamente o campo de relacionamento com tbl_usuarios
    usu_codigo = models.ForeignKey(
    tbl_usuarios, on_delete=models.CASCADE, related_name='tarefas', db_column='usu_codigo'
)

    def __str__(self):
        return self.tar_descricao
    
    
    
    def save(self, *args, **kwargs):
        print(f"Salvando tarefa: {self.tar_descricao}, {self.tar_setor}")
        super().save(*args, **kwargs)


    class Meta:
        db_table = 'tbl_tarefas'
