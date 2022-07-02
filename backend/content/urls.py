from django.urls import path, include
from .views import *
urlpatterns = [
    path('tag', TagListView.as_view()),
    path('article', ArticleListView.as_view()),
    path('article/<int:pk>', ArticleView.as_view()),
]