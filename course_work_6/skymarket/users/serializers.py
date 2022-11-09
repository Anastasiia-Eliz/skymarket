from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from .models import User


class UserRegistrationSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "phone", "password", "email")

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(user.password)
        user.save()

        return user


class UserCurrentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'first_name', 'last_name', 'phone')