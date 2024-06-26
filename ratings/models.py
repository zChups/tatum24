from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class Rating(models.Model):
    LIKE = 'like'
    DISLIKE = 'dislike'
    CHOICES = [
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
    ]

    snippet = models.ForeignKey('snippets.Snippet', related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)
    rating = models.CharField(max_length=7, choices=CHOICES)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('snippet', 'user')  # Ensure each user can rate a snippet only once

    def __str__(self):
        return f"{self.user.username} rated '{self.snippet.title}' as {self.get_rating_display()}"
