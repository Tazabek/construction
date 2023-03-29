from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Messages, Subscribe

class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ('name', 'email', 'text',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'name-email', 'placeholder': 'Имя'}),
            'email': forms.EmailInput(attrs= {'class': 'name-email', 'placeholder': 'Email Address'}),
            'text': forms.Textarea(attrs= {'class': 'name-email', 'placeholder': 'Сообщение'}),
        }

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput(attrs={
            'class': 'form-control', 'placeholder': 'Email Адрес'
            })
        }