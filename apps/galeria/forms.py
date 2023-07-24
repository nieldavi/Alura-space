from apps.galeria.models import Fotografia
from django import forms


class FotografiaForms(forms.ModelForm):
    class Meta:
        ''' Meta dodos da classe FotografiaForms'''
        model = Fotografia
        labels = {
            'descricao': 'Descrição',
            'data_fotografia': 'Data da Registro',
            'usuario': 'Usuário',
            'categoria': 'Categoria',

        }
        exclude = ['publicada']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'legenda': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'data_fotografia': forms.DateTimeInput(
                format='%d/%m/%Y',
                attrs={
                    'type': 'date',
                    'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
        }
