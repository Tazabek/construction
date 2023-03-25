from django.urls import path
from apps.blog import views
from apps.blog.views import *

urlpatterns = [
    path('blogs/', blog, name='blogs'),
    path('blogs/blog-dateil/<str:slug>', single_blog, name = 'blog_detail'),
    path('blogs/category/<str:slug>', categy, name='blog_cats'),
]