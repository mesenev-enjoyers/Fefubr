from rest_framework import generics
from .serializers import *
from .models import *


class TagListView(generics.ListCreateAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
