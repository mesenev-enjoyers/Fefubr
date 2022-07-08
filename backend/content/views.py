from rest_framework import generics, mixins, permissions

from users.models_subscription import UserSubscribtion, TagSubscribtion
from .serializers import *
from .models import *
from .likes import ContentAPIMixin




class ArticleListView(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        query = Article.objects.all()
        tag = self.request.query_params.get('tag')  # гет параметры
        user = self.request.query_params.get('user')
        rating = self.request.query_params.get('rating')

        if user is not None:
            query = query.filter(creator=user)
        if tag is not None:
            query = query.filter(tags=tag)
        if rating is not None:
            query = query.order_by('-rating')
        return query


class ArticleView(ContentAPIMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class TagListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class TagView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class CommentListView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        query = Comment.objects.all()
        article = self.request.query_params.get('article')
        if article is not None:
            query = query.filter(article_id=article)
        return query


class CommentView(ContentAPIMixin):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class MyArticleView(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        subs = UserSubscribtion.objects.filter(user=user)
        subs_id = []
        for i in subs:
            subs_id.append(i.subscribe.id)

        tags = TagSubscribtion.objects.filter(user=user)
        tags_id = []
        for i in tags:
            tags_id.append(i.tag_subscribe_id)

        query = Article.objects.filter(tags__in=tags_id) | Article.objects.filter(creator_id__in=subs_id)

        rating = self.request.query_params.get('rating')
        if rating is not None:
            query = query.order_by('-rating')

        return query.distinct()


