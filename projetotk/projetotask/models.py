from django.db import models

class tbl_usuarios(models.Model):
 usu_nome = models.CharField(max_length=40)
 usu_email = models.CharField(max_length=30)
 
class tbl_tarefas(models.Model):
    tar_descricao= models.CharField(max_length=100)
    tar_setor= models.CharField(max_length=100)
    tar_prioridade= models.CharField(max_length=100)
    tar_status= models.CharField(max_length=100)
    tar_data= models.CharField(max_length=100)
    
 
 
objetos = models.Manager()