from django.urls import path
from apps.team import views
from apps.team.views import *

urlpatterns = [
    path('team/', team, name='team'),
    path('team/details/<str:slug>', team_detail, name='expert')
]
