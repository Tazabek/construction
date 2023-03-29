from django.urls import path
from apps.careers import views
from apps.careers.views import *

urlpatterns = [
    path('careers/', careers, name='careers'),
    path('apply/', careers, name='apply')
]
