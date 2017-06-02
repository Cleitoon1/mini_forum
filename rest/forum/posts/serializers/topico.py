from rest_framework import serializers
from forum.posts.models.topico import Topico


class TopicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topico
        fields = '__all__'