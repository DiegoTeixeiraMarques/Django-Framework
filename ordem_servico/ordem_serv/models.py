from django.db import models

class TipoServico(models.Model):
    descricao = models.CharField(max_length=50)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descricao


