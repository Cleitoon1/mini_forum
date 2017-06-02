from rest_framework import generics

from forum.usuarios.models.user import User


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = User

    def perform_create(self, serializer):
        serializer.save()