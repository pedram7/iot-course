from django.contrib.auth import authenticate

from rest_framework import serializers
from .models import Guard


class GuardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guard
        fields = ['name', 'staff_id', 'date_joined']


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(label="شناسه کاربری")
    password = serializers.CharField(label="رمز عبور", style={'input_type': 'password'}
                                     , write_only=True)

    def validate(self, attrs):
        user = authenticate(username=attrs['username'], password=attrs['password'])

        if not user:
            raise serializers.ValidationError('Incorrect email or password.')

        if not user.is_active:
            raise serializers.ValidationError('User is disabled.')

        return {'user': user}