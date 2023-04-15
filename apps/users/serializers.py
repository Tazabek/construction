from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only= True)

    class Meta:
        model = User
        fields = (
            'id', 
            'email', 
            'profile_image',
            'password',
            'confirm_password'
        )

    def create(self, validated_data):
        if not validated_data['confirm_password']:
            raise serializers.ValidationError('Confirm your password')
        if validated_data['password'] != validated_data['confirm_password']:
            raise serializers.ValidationError('passwords are not same!')
        user = User(
            username = validated_data['username'],
            email = validated_data['email'],
            profile_image = validated_data['prosile_image'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
    

class UpdatePasswordSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only= True)

    class Meta:
        model = User
        fields = [
            'password',
            'confirm_password'
        ]

    def update(self, instance, validated_data):
        if not validated_data['confirm_password']:
            raise serializers.ValidationError('Confirm your password')
        if validated_data['password'] != validated_data['confirm_password']:
            raise serializers.ValidationError('passwords are not same!')
        instance.set_password(validated_data['password'])
        instance.save()
        return instance