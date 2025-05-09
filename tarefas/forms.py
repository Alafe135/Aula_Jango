from django import forms

from .models import Tarefas

class Tarefaform(forms.ModelForm):
    class Meta:
        model = Tarefas
        fields = ('titulo', 'descricao')