from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from content.likes import Like
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
    rating = models.IntegerField(default=0, blank=True)
    picture = models.ImageField(null=True, blank=True)
    likes = GenericRelation(Like)

    def __str__(self):
        return self.name

    class Meta:
        ordering =['-date', '-rating']


class Comment(models.Model):
    creator = models.ForeignKey(CustomUser, related_name='comment_creator', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, related_name='comment_article_name', on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0, blank=True)
    likes = GenericRelation(Like)
    reply = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.article.name) + ": " + str(self.creator.username)


