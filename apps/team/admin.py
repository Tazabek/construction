from django.contrib import admin
from .models import *

class SkillInline(admin.TabularInline):
    model = Skills
    extra = 1

class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1

class MemberAdmin(admin.ModelAdmin):
    inlines = [SkillInline, ExperienceInline ]
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Member, MemberAdmin)