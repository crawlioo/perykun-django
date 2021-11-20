from django.contrib import admin

# Register your models here.
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published')
    date_hierarchy = 'published'
    search_fields = ('title', 'content')
