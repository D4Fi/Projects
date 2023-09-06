from django import forms

class ContactForms(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    age = forms.IntegerField(label='age')
