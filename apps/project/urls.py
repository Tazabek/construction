from django.urls import path
from apps.project import views
from apps.project.views import *

urlpatterns = [
    path('projects/', project, name='project'),
    path('projects/single_project/<str:slug>/', single_project, name = 'single_project')
]
