from django.urls import path
from .views import *
urlpatterns = [
    path('subscribe', SubscribeListView.as_view()),
    path('subscribe/<int:pk>', SubscribeListView.as_view()),
    path('tag', TagsListView.as_view()),
    path('tag/<int:pk>', TagsListView.as_view()),
]