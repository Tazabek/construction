from django.shortcuts import render
from .models import *
from apps.homepage.models import *

def careers(request):
    settings = Settings.objects.latest('id')
    benefits = Benefits.objects.all()
    vacancy = Vacancy.objects.all()
    context = {
        'settings': settings,
        'benefits': benefits,
        'vacancy': vacancy,
    }
    return render(request, 'careers.html', context)