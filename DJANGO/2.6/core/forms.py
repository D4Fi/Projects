from django import forms

class FormsProduto(forms.ModelForm):
    nome = forms.CharField(max_length=30)
    valor = forms.DecimalField(max_digits=2, decimal_places=2)
    estoque = forms.IntegerField()
    img_produto = forms.ImageField()
