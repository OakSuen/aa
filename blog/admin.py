from django.contrib import admin
from .models import Post, Category, Tag, News


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish', 'category')
    list_filter = ('created', 'publish', 'author', 'category')
    search_fields = ('title', 'body')
    date_hierarchy = 'publish'
    ordering = ['publish']


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish')
    list_filter = ('title', 'publish')
    search_fields = ('title', 'body')
    date_hierarchy = 'publish'
    ordering = ['publish']

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(News)
