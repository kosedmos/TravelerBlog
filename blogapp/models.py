from django.db import models

# Create your models here.


class Article(models.Model):
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    author = models.ForeignKey('auth.User', default=1)
    title = models.CharField(max_length=200, blank=True)
    content = models.TextField()

    class Meta:
        ordering = ('created',)