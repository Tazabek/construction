from django.urls import path
from apps.history import views
from apps.history.views import *

urlpatterns = [
    path('history/', history, name = 'history')
]
