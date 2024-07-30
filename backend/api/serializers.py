from django.conf import settings
from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model
    """

    class Meta:
        model = CustomUser
        fields = ("id", "username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """
        Create new user with encrypted password and return it
        :param validated_data:
        :return:
        """
        user = CustomUser(
            email=validated_data["email"], username=validated_data["username"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

    class Meta:
        """
        Serializer for User model
        """

        model = CustomUser
        fields = ("id", "username", "email")
