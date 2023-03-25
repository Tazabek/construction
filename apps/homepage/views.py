from django.shortcuts import render
from .models import *
from apps.team.models import *
from apps.blog.models import *
from apps.service.models import *
from apps.project.models import *

def homepage(request):
    settings = Settings.objects.latest('id')
    slides = Slides.objects.all()
    services = Services.objects.all().order_by('id')[:3]
    projects = Projects.objects.all().order_by('-id')[:6]
    experts = Member.objects.all()
    blog = Blogs.objects.all().order_by('-id')[:3]
    posts = Blogs.objects.all().order_by('-count')[:2]
    count = Projects.objects.count()
    count2 = Member.objects.count()
    context = {
        'settings': settings,
        'slides': slides,
        'services': services,
        'projects': projects,
        'experts': experts,
        'blogs': blog,
        'posts': posts,
        'count': count,
        'count2': count2,
    }
    return render(request, 'index.html', context)



def contacts(request):
    contacts = Settings.objects.latest('id')
    context = {
        'contacts': contacts,
        'home': 'Главная',
        'next': 'Контакты',
    }
    return render(request, 'contact-2.html', context)