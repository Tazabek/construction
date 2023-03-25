from django.shortcuts import render
from .models import *
from apps.homepage.models import *

def project(request):
    projects = Projects.objects.all()
    category = Category.objects.all()
    settings = Settings.objects.latest('id')
    context = {
        'projects': projects,
        'category': category,
        'settings': settings,
        'home': 'Главная',
        'next': 'Проекты'
    }
    return render(request, 'projects/project.html', context)

def single_project(request, slug):
    projects = Projects.objects.get(slug=slug)
    images = ProjectImages.objects.filter(project = projects)
    settings = Settings.objects.latest('id')
    context = {
        'projects': projects,
        'settings': settings,
        'images': images,
        'home': 'Главная',
        'next': 'Детали проекта'
    }
    return render(request, 'projects/project-details.html', context)
    

