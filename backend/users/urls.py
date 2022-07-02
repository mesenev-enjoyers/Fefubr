from django.urls import path
from .views import *
urlpatterns = [
    path('subscribe/', SubscribeListView.as_view()),
    path('subscribe/<int:pk>', SubscribeView.as_view()),
    path('tag/', TagsListView.as_view()),
    path('tag/<int:pk>', TagsView.as_view()),
]