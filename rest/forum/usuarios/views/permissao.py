from rest_framework import generics

from forum.usuarios.models.permissao import Permissao
from forum.usuarios.serializers.permissao import PermissaoSerializer


class PermissaoView(generics.ListCreateAPIView):
    queryset = Permissao.objects.all()
    serializer_class = PermissaoSerializer

    def perform_create(self, serializer):
        serializer.save()