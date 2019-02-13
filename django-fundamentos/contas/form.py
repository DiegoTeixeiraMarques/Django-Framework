from django.forms import ModelForm                             # Classe que implementa as facilidades do Form em python
from .models import Transacao                                  # Model que vai participar do Formulário

class TransacaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = ['data', 'descricao', 'valor', 'observacoes', 'categoria']      # Fields que serão mostrados no formulário