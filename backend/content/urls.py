from django.urls import path, include
from .views import *
urlpatterns = [
    path('tag', TagListView.as_view() ),
]