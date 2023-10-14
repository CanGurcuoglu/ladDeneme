from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from rest_framework import generics 
from rest_framework.generics import get_object_or_404

from missions.api.serializers import UserSerializer, MissionSerializer
from missions.models import User, Mission


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MissionCreateAPIView(generics.CreateAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    def perform_create(self, serializer):
        user_pk = self.kwargs.get('user_pk')
        user = get_object_or_404(User, pk=user_pk)
        serializer.save(user=user)

class MissionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer