from django.db import models

from users.models import CustomUser


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    creator = models.ForeignKey(CustomUser, related_name='article_creator', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    content = models.CharField(max_length=20000)
    date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    rating = models.IntegerField(default=0, null=True, blank=True)
    picture = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
