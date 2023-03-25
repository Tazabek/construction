from django.shortcuts import render
from .models import *
from apps.homepage.models import *


def team(request):
    team = Member.objects.all()
    settings = Settings.objects.latest('id')
    context = {
        'team':team,
        'settings': settings,
        'home': 'Главная',
        'next': 'Наша команда',
    }
    return render(request, 'team/team.html', context)

def team_detail(request, slug):
    settings = Settings.objects.latest('id')
    member = Member.objects.get(slug = slug)
    skill = Skills.objects.filter(member = member)
    expers = Experience.objects.filter(member = member)

    context = {
        'member': member,
        'settings': settings,
        'skills': skill,
        'expers': expers,
        'home': 'Главная',
        'next': 'Наша команда',
    }
    return render(request, 'team/team-details.html', context)