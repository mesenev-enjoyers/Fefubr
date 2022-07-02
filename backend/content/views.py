from rest_framework import generics, mixins


from .serializers import *
from .models import *
from .likes import  ContentAPIMixin


class TagListView(generics.ListCreateAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class ArticleListView(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        query = Article.objects.all()
        tag = self.request.query_params.get('tag')
        user = self.request.query_params.get('user')
        if user is not None:
            query = query.filter(creator=user)
        if tag is not None:
            query = query.filter(tags=tag)
        return query


class ArticleView(ContentAPIMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


