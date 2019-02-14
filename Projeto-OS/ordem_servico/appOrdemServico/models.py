from django.db import models


class TipoServico(models.Model):
    tipo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=200)

    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name = 'Tipos de serviço'


class OrdemServico(models.Model):
    tipo_servico = models.ForeignKey(TipoServico, on_delete=models.CASCADE)
    descricao = models.TextField(max_length=220)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Ordem de serviço'