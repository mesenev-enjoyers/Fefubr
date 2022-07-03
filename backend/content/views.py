from rest_framework import generics, mixins


from .serializers import *
from .models import *
from .likes import ContentAPIMixin


class TagListView(generics.ListCreateAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class ArticleListView(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer

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


class CommentListView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        query = Comment.objects.all()
        article = self.request.query_params.get('article')
        if article is not None:
            query = query.filter(article_id=article)
        return query


class CommentView(ContentAPIMixin):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


