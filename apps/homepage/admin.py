from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Settings)
admin.site.register(Slides)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Messages)
