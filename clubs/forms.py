from django import forms
from .models import Criticism

class CriticismForm(forms.ModelForm):
    class meta:
        model = Criticism
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={
                'rows': 5,
                'cols': 50,
                'placeholder': 'write your criticism here ...'
            }),
        }