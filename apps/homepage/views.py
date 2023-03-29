from django.shortcuts import render, redirect
from .models import *
from apps.team.models import *
from apps.blog.models import *
from apps.service.models import *
from apps.project.models import *
from .forms import *

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
    count3 = Messages.objects.count()
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            s = Subscribe(email=email)
            s.save()
            return render(request, 'subs.html')
    else:
        form = SubscribeForm()
    context = {
        'settings': settings,
        'slides': slides,
        'services': services,
        'projects': projects,
        'experts': experts,
        'blogs': blog,
        'posts': posts,
        'form': form,
        'count': count,
        'count2': count2,
        'count3': count3,
    }
    return render(request, 'index.html', context)

def massege(request):
    return render(request, '404.html')


def contacts(request):
    contacts = Settings.objects.latest('id')
    form = MessageForm(request.POST)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']

            m = Messages(name=name, email=email, text=text)
            m.save()
        return redirect('massege')
    else:
        form = MessageForm()
    
    context = {
        'contacts': contacts,
        'form': form,
        'home': 'Главная',
        'next': 'Контакты',
    }
    return render(request, 'contact-2.html', context)

def search(request):
    query = request.GET.get('search field')
    services = Services.objects.filter(name__contains=query)
    blogs = Blogs.objects.filter(title__contains=query)
    projects = Projects.objects.filter(name__contains=query)
    team = Member.objects.filter(name__contains=query)
    context = {
        'services': services,
        'projects': projects,
        'experts': team,
        'blogs': blogs,
    }
    return render(request, 'search.html', context)