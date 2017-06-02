from rest_framework import generics

from forum.posts.models.post import Post
from forum.posts.serializers.post import PostSerializer


class PostView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save()