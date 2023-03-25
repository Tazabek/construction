from django.contrib import admin
from .models import *

class ImageInlines(admin.TabularInline):
    model = ProjectImages
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ImageInlines]
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Projects, ProjectAdmin)
