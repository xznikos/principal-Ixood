from django import forms
from .models import EncomendasModel

class EncomendasForm(forms.ModelForm):
    class Meta:
        model = EncomendasModel
        fields = ['nome', 'preco', 'imagem']