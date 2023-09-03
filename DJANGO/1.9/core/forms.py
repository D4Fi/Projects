from django import forms
from . import models

class FormPessoa(forms.ModelForm):
    class Meta:
        model = models.Pessoa
        fields = ('nome', 'idade')
