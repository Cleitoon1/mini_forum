from rest_framework import generics

from rest.forum.posts.models.resposta import Resposta
from rest.forum.posts.serializers.resposta import RespostaSerializer


class RespostaView(generics.ListCreateAPIView):
    queryset = Resposta.objects.all()
    serializer_class = RespostaSerializer

    def perform_create(self, serializer):
        serializer.save()