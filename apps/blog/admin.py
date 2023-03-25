from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *

class CommentInline(admin.TabularInline):
    model = Commenst
    extra = 1

class ImagesInline(admin.TabularInline):
    model = Images
    extra = 1
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100px">')

class BlogAdmin(admin.ModelAdmin):
    inlines = [ImagesInline, CommentInline]
    prepopulated_fields = {'slug':('title',)}
    list_filter = ('category',)

admin.site.register(Blogs, BlogAdmin)
admin.site.register(Commenst)
