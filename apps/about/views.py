from django.shortcuts import render
from .models import *
from apps.blog.models import *
from apps.homepage.models import *
from apps.service.models import *

def about(request):
    about = About.objects.latest('id')
    service = Services.objects.all().order_by('id')[:3]
    blogs = Blogs.objects.all().order_by('-id')[:3]
    settings = Settings.objects.latest('id')
    home = 'Главная'
    next = 'О нас'
    context = {
        'about': about,
        'settings': settings,
        'home': home,
        'next': next,
        'service': service,
        'blogs': blogs,
    }
    return render(request, 'about.html', context)
