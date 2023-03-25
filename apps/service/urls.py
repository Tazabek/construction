from django.urls import path
from apps.service import views
from apps.service.views import *

urlpatterns = [
    path('service/', services, name='service'),
    path('service/service-details/<str:slug>', single_service, name='single_service'),
    path('service/category/<str:slug>', category, name='category')
]
