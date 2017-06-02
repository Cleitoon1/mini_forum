from rest_framework import generics

from forum.posts.models.topico import Topico
from forum.posts.serializers.post import PostSerializer


class TopicoView(generics.ListCreateAPIView):
    queryset = Topico.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save()