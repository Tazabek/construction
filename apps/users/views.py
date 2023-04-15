from django.shortcuts import render
from rest_framework import generics, viewsets
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser
from apps.blog.permissions import *

from .serializers import *

User = get_user_model()

class UserAPIView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_by_action = {
        'list': [IsAuthenticatedOrReadOnly],
        'create': [AllowAny],
        'retrieve': [IsAuthenticatedOrReadOnly],
        'update': [IsOwner | IsAdminUser],
        'delete': [IsOwner | IsAdminUser],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
        
    

class PasswordAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdatePasswordSerializer
    permission_classes = [IsOwner | IsAdminUser]

