from django.shortcuts import render, redirect
from .models import *
from .forms import *
from apps.homepage.models import *

def careers(request):
    settings = Settings.objects.latest('id')
    benefits = Benefits.objects.all()
    vacancy = Vacancy.objects.all()
    form = ApplyForm(request.POST)
    if request.method == "POST":
        form = ApplyForm(request.POST)
        if form.is_valid():
            name1 = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            post = request.POST.get('post_job')
            image = request.FILES['photo']            
            text = form.cleaned_data['text']

            a = Apply(name=name1, email=email, phone=phone, post=post, image=image, text=text)
            a.save()

            return render(request, '404.html')
    else:
        form = ApplyForm()
    context = {
        'settings': settings,
        'benefits': benefits,
        'vacancy': vacancy,
        'form': form,
        'home': 'Главная',
        'next': 'Карьера',
    }
    return render(request, 'careers.html', context)