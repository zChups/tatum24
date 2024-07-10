from django.contrib.auth.models import User
from django.db import models
from snippets.models import Snippet


class Bookmark(models.Model):
    snippet = models.ForeignKey(Snippet, related_name='bookmarks', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='bookmarks', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-user']

    def __str__(self):
        return f"{self.snippet.title} bookmarked by {self.user.username}"

    def save(self, *args, **kwargs):
        super(Bookmark, self).save(*args, **kwargs)
