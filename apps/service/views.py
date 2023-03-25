from django.shortcuts import render
from .models import *
from apps.homepage.models import *

def services(request):
    services = Services.objects.all()
    adver = Advertisement.objects.latest('id')
    settings = Settings.objects.latest('id')
    context = {
        'services': services,
        'adver': adver,
        'settings': settings,
        'home': 'Главная',
        'next': 'Услуги',
    }
    return render(request, 'service/service.html', context)

def single_service(request, slug):
    service = Services.objects.get(slug=slug)
    category = Category.objects.all()
    settings = Settings.objects.latest('id')
    context = {
       'service':service,
       'category': category,
       'settings': settings,
       'home': 'Главная',
       'next': 'Об услуге',
    }
    return render(request, 'service/service-details.html', context)
    
def category(request, slug):
    categor = Category.objects.get(slug = slug)
    services = Services.objects.filter(category = categor)
    adver = Advertisement.objects.latest('id')
    settings = Settings.objects.latest('id')
    
    context = {
        'services': services,
        'adver': adver,
        'settings': settings,
        'home': 'Главная',
        'next': 'Услуги',
    }
    return render(request, 'service/service.html', context)