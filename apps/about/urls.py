from django.urls import path
from apps.about import views
from apps.about.views import *

urlpatterns = [
    path('about/', about, name='about')
]