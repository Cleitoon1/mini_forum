from rest_framework import generics

from forum.usuarios.models.perfil import Perfil
from forum.usuarios.serializers.perfil import PerfilSerializer


class PerfilView(generics.ListCreateAPIView):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

    def perform_create(self, serializer):
        serializer.save()