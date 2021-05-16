from django.db.models import fields
from rest_framework import serializers
from profiles.models import UserProfile
from .models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('name',)
        

class UserRegistrationSerializer(serializers.ModelSerializer):
    profile = UserSerializer(required=False)
    class Meta:
        model = User
        fields = ('email', 'password', 'profile')

    def create(self, validated_data):
        profile_data=validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(
            user=user,
            name=profile_data['name']
        )
        return user

        return super().create(validated_data)