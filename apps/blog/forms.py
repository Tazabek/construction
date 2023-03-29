from django import forms
from .models import *

class NewsForm(forms.ModelForm):
    class Meta:
        model = Commenst
        fields = ('name', 'comment',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Сообщение'}),
            }
    
