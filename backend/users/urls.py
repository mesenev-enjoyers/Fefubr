from django.urls import path
from .views import *
urlpatterns = [
    path('subscribe', SubscribeListView.as_view()),
    path('subscribe/<int:pk>', SubscribeListView.as_view()),

]