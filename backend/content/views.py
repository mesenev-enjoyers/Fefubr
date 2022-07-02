from rest_framework import generics
from rest_framework.response import Response

from .serializers import *
from .models import *
from .likes import add_like, remove_like

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


class ArticleView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        like = self.request.query_params.get('like')
        unlike = self.request.query_params.get('unlike')
        if like is not None:
            add_like(instance, self.request.user)

        if unlike is not None:
            remove_like(instance, self.request.user)
        return Response(serializer.data)
