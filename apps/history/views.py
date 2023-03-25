from django.shortcuts import render
from .models import History
from apps.homepage.models import *

def history(request):
    history = History.objects.all()
    settings = Settings.objects.latest('id')
    context = {
        'history': history,
        'settings': settings,
        'home': 'Главная',
        'next': 'Наша история',
    }
    return render(request, 'company-story.html', context)
