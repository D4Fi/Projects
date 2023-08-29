from django import forms
from . import models




class UserPost(forms.ModelForm):

    class Meta:
        model = models.Post
        fields = ('nome', 'idade')
