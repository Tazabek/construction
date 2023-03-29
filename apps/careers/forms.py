from django import forms
from .models import *

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ('name', 'email', 'phone', 'text',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ф.И.О'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email адрес', 'type': 'email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тел. номер'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ваше сообшение'}),
        }
