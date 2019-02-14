from django.db import models

class TipoServico(models.Model):
    #dt_criacao = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=50, blank=False)
    descricao = models.TextField(max_length=200, blank=False)

    def __str__(self):
        return self.tipo


