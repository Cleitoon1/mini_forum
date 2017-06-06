from rest_framework import generics

from rest.forum.posts.models.post import Post
from rest.forum.posts.serializers.post import PostSerializer


class PostView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save()