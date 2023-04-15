from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('apps.homepage.urls')),
    path('', include('apps.team.urls')),
    path('', include('apps.blog.urls')),
    path('', include('apps.about.urls')),
    path('', include('apps.careers.urls')),
    path('', include('apps.history.urls')),
    path('', include('apps.service.urls')),
    path('', include('apps.project.urls')),
    path('', include('company.routers')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
