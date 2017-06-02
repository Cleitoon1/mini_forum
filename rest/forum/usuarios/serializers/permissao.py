from rest_framework import serializers

from forum.usuarios.models.permissao import Permissao


class PermissaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permissao
        fields = '__all__'