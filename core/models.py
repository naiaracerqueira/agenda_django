from django.db import models
from django.contrib.auth.models import User

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True) #pode ser branco ou nulo
    data_evento = models.DateTimeField(verbose_name="Data do Evento") #nao pode ser nulo
    data_criacao = models.DateTimeField(auto_now=True, verbose_name="Data de Criação") #pega data de registro
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #pega usuarios do admin... se usuario for excluido

    class Meta:
        db_table = 'evento' #exigindo que tabela chame evento

    def __str__(self):
        return self.titulo #sempre que chamar o titulo, ele vai trazer o nome do objeto/titulo
