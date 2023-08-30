from django import forms
from . import models

class UserPost(forms.ModelForm):

    class Meta:
        model = models.Pessoa
        fields = ('nome', 'idade')
