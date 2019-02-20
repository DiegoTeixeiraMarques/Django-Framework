from django.db import models

# ---------------------------------------------------------------- #

class TipoServico(models.Model):
    descricao = models.CharField(max_length=60, blank=False, null=False)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Tipo de serviço'
        verbose_name_plural = 'Tipos de serviços'

# ---------------------------------------------------------------- #

class Setor(models.Model):
    centro_custo = models.IntegerField(unique=True)
    nome = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'

# ---------------------------------------------------------------- #

class Ugb(models.Model):
    codigo = models.IntegerField(unique=True)
    nome = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'UGB'
        verbose_name_plural = 'UGBs'

# ---------------------------------------------------------------- #


class Cargo(models.Model):
    descricao = models.CharField(max_length=60, blank=False, null=False)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

# ---------------------------------------------------------------- #


class Funcionario(models.Model):
    matricula = models.PositiveIntegerField(unique=True)
    nome = models.CharField(max_length=60)
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

# ---------------------------------------------------------------- #

