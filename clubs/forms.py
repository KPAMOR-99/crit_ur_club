from django import forms
from .models import Criticism

class CriticismForm(forms.ModelForm):
    class Meta:
        model = Criticism  # Link the form to the Criticism model
        fields = ['comment']  
        widgets = {
            'comment': forms.Textarea(attrs={
                'rows': 5,
                'cols': 50,
                'placeholder': 'Write your criticism here...'
            }),
        }