from django import forms

class formsProduto(forms.ModelForm):
    logo = forms.ImageField(allow_empty_file='uploads/')
    produto = forms.CharField(max_length=20)
    valor = forms.FloatField()
    estoque = forms.IntegerField()

