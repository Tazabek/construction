from django.contrib import admin
from .models import *

class ServicesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    


admin.site.register(Services, ServicesAdmin)
admin.site.register(Advertisement)
