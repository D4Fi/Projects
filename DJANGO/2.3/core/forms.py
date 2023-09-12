from django import forms

class ContactForms(forms.Form):
    name = forms.CharField(label='Name')
    email = forms.EmailField(label='E-mail')
    subject = forms.CharField(label='Subject')
    message = forms.CharField(label='Message', widget=forms.Textarea())
