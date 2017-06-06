from rest_framework import serializers

from rest.forum.usuarios.models.permissao import Permissao


class PermissaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permissao
        fields = '__all__'