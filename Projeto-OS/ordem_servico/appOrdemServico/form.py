from django.forms import ModelForm                             # Classe que implementa as facilidades do Form em python
from .models import TipoServico, OrdemServico

class TipoServicoForm(ModelForm):
    class Meta:
        model = TipoServico
        fields = ['tipo', 'descricao']