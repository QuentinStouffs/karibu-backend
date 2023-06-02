from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User 
        fields = ('id', 'name', 'username', 'password', 'last_name', 'first_name', 'email')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user
    
class UserSerializerWOpassword(serializers.ModelSerializer):

    class Meta:
        model = User 
        fields = ('id', 'name', 'username', 'last_name', 'first_name', 'email')

    def create(self, validated_data):
       
        user = super().create(validated_data)
        user.save()
        return user
    