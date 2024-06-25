from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count, Sum


class SnippetManager(models.Manager):
    @staticmethod
    def top_authors():
        return User.objects.annotate(score=Count('snippets')).order_by('-score')

    def top_rated(self):
        return self.annotate(score=Sum('rating__rating')).order_by('-score')


class LanguageManager(models.Manager):
    @staticmethod
    def top_languages():
        return User.objects.annotate(score=Count('snippets')).order_by('-score')
