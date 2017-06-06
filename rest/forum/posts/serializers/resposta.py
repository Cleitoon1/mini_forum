from rest_framework import serializers
from rest.forum.posts.models.resposta import Resposta


class RespostaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resposta
        fields = '__all__'
        read_only_fields = ('data_criacao',)