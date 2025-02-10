from django.contrib.auth import (get_user_model, authenticate)
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.translation import gettext as _


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['uuid','email', 'password', 'name', 'is_active', 'is_superuser']
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 5},
            'email': {'required': False},
            'is_active': {'read_only': True},
            'is_superuser': {'read_only': True}
        }

    def validate(self, attrs):
        email = attrs.get('email')

        if not email:
            raise serializers.ValidationError({
                'non_field_errors': ['Email must be provided.']
            })

        if email:
            if get_user_model().objects.filter(email=email).exists():
                raise serializers.ValidationError({
                    'email': ['User with this email already exists, please login.']
                })

        return attrs

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type':'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):

        email = attrs.get('email')

        password = attrs.get('password')
        print(password)

        if not email or not password:
            raise serializers.ValidationError({'Please enter email and password'}, code='authorization')

        user = None
        if '@'in email:
            user = get_user_model().objects.filter(email=email).first()
        
        if user is not None:
            print(user)
            user = authenticate(
                request=self.context.get('request'),
                username=user.email,
                password= password,
            )
            if not user:
                raise serializers.ValidationError({'Please enter valid email or password'}, code='authorization')

            refresh = RefreshToken.for_user(user)
            tokens = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }

            return {
                'user': user,
                'tokens': tokens
            }

        else:
            raise serializers.ValidationError({'User does not exist, please register'}, code='authorization')

