from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

'''This class is used to serialize the user deatils'''
class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model=User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']
        
        
    def create(self, validated_data):
        
        validated_data['password'] = make_password(validated_data.get('password'))
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user
        
'''This class is for login'''
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
