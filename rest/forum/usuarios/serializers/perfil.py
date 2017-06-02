from rest_framework import serializers

from forum.usuarios.models.perfil import Perfil


class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'