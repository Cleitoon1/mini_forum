import hashlib

from rest_framework import serializers
from rest.forum.usuarios.models.user import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            validated_data['password'] = hashlib.md5(validated_data.get('password', '').encode()).hexdigest()
            return super(UserSerializer, self).create(validated_data)

        def update(self, instance, validated_data):
            validated_data['password'] = hashlib.md5(validated_data.get('password', '').encode()).hexdigest()
            return super(UserSerializer, self).update(instance, validated_data)