from rest_framework import serializers
from .models import User


class UserLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'password']


class UserRegisterSerializer(serializers.ModelSerializer):
    USER_TYPE_CHOICE = [
        ('student', 'Student'),
        ('parent', 'Parent')
    ]
    password = serializers.CharField(write_only=True)
    user_type = serializers.ChoiceField(choices=USER_TYPE_CHOICE)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'password','user_type']
