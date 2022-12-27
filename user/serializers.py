from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    # producers = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_auto_show', 'is_customer', 'is_producer']

