from django.db import models

class TipoServico(models.Model):
    descricao = models.CharField(max_length=60)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Tipo de serviço'
        verbose_name_plural = 'Tipos de serviços'
