from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.blog.views import *
from apps.users.views import UserAPIView, PasswordAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(
    'post',
    BlogViewSet, 
    basename='post'
)

router.register(
    'image',
    PostImageAPIView,
    basename='image'
)

router.register(
    'like',
    LikeAPIView,
    basename='like'
)

router.register(
    'user',
    UserAPIView,
    basename='user'
)

urlpatterns = [
    path('user/<int:pk>/change_password/', PasswordAPIView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls