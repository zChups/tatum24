# admin.py

from django.contrib import admin
from snippets.models import Snippet, Language

admin.site.register(Snippet)
admin.site.register(Language)


class SnippetAdmin(admin.ModelAdmin):
    list_display = ('content', 'author')
    search_fields = ('content', 'author__username')


class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'snippet', 'rating', 'date')
