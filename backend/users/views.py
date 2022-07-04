from rest_framework import generics
from .serializers import *
from .models_subscription import *
from .permissions import IsOwnerOrReadOnly


class SubscribeListView(generics.ListCreateAPIView):
    serializer_class = UserSubscriptionSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        user_request = self.request.query_params.get('user')
        if user_request is not None:
            return UserSubscribtion.objects.filter(user_id=user_request)
        return UserSubscribtion.objects.filter(user_id=self.request.user)


class SubscribeView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserSubscribtion.objects.all()
    serializer_class = UserSubscriptionSerializer
    permission_classes = [IsOwnerOrReadOnly]


class TagsListView(generics.ListCreateAPIView):
    queryset = TagSubscribtion.objects.all()
    serializer_class = TagSubscriptionSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        user_request = self.request.query_params.get('user')
        if user_request is not None:
            return TagSubscribtion.objects.filter(user_id=user_request)
        return TagSubscribtion.objects.filter(user_id=self.request.user)


class TagsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TagSubscribtion.objects.all()
    serializer_class = TagSubscriptionSerializer
    permission_classes = [IsOwnerOrReadOnly]


class UsersListView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = CustomUser.objects.all()
        top = self.request.query_params.get('top')
        if top is not None:
            top = int(top)
            queryset = queryset.filter('-rating')[:top]
            return queryset


class UsersView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer




