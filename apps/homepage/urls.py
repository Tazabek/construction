from django.urls import path
from apps.homepage import views
from apps.homepage.views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('contact/', contacts, name = 'contact')
]
