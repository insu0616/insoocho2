from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    content = models.TextField(max_length=300)
    hits = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def hit(self):
        self.hits += 1
        self.save()
        return self.hits

class Comment(models.Model):
    article = models.ForeignKey(Article)
    content = models.TextField(max_length=200)

    def __str__(self):
        return self.content