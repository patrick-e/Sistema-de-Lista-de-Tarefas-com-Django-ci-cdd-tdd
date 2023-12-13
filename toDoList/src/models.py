from django.db import models

# Create your models here.

class Task(models.Model):
    titulo_tarefa = models.CharField(max_length=255)
    descricao = models.CharField(blank=True, null=True,max_length=1000)
    
    def __str__(self):
        return self.titulo_tarefa