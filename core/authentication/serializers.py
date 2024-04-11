from .models import AppUser, Profile
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.serializers import PasswordField
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    password = PasswordField(required=True)
    password2 = PasswordField(required=True)
    username = serializers.CharField(write_only=True, required=False)
    class Meta:
        model = AppUser
        fields = ['password', 'password2', 'first_name', 'last_name', 'phone', 'email', 'username']


    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        from rest_framework_simplejwt.tokens import RefreshToken
        ret['token'] = {
            'refresh': f'{RefreshToken.for_user(instance)}',
            'access_token': f'{RefreshToken.for_user(instance).access_token}'
        }
        return ret

    def create(self, validated_data):
        user = AppUser.objects.create(
            username=validated_data['phone'],
            phone=validated_data['phone'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = PasswordField(required=True)
    phone = serializers.CharField(required=False)
    class Meta:
        model = AppUser
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'phone']

    def create(self, validated_data):
        user: AppUser = authenticate(**validated_data)
        if not user or not user.is_active:
            raise AuthenticationFailed('Username or password is incorrect.')
        return user

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        from rest_framework_simplejwt.tokens import RefreshToken
        ret['token'] = {
            'refresh': f'{RefreshToken.for_user(instance)}',
            'access_token': f'{RefreshToken.for_user(instance).access_token}'
        }
        return ret


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField(required=False, write_only=True)
    class Meta:
        model = Profile
        fields = ('__all__')

    def validate(self, attrs):
        attrs['user'] = self.context.get("request").user
        return  attrs