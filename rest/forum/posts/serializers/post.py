from rest_framework import serializers
from rest.forum.posts.models.post import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('data_criacao', 'data_publicacao')

