from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Artisan, Type
from .functions import attempt_json_deserialize
from karibu_backend.models import User
import json
import googlemaps
import sys

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Type
        fields="__all__"
class ArtisanSerializer(serializers.ModelSerializer):
    type=TypeSerializer(many=True, read_only=True)
    user=serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    class Meta:
        model = Artisan 
        fields="__all__"

class ArtisanSerializerWOLatLon(serializers.ModelSerializer):
    type=TypeSerializer(many=True, read_only=True)
    user=serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    class Meta:
        model = Artisan 
        exclude = ('latitude', 'longitude')


    def create(self, validated_data):
        request=self.context['request']

        user=request.data.get('user')
        user=attempt_json_deserialize(user, expect_type=int)
        validated_data['user']=User.objects.get(id=user)
        
        full_address=request.data.get('address') +" " + request.data.get('zipcode') + " " + request.data.get('city')
        gmaps=googlemaps.Client(key='AIzaSyBoaHIOTYN8Q6aXWWh955bgbTINRiP0CXM')
        geocode_result=gmaps.geocode(full_address)
       
        validated_data['latitude']=geocode_result[0]['geometry']['location']['lat']
        validated_data['longitude']=geocode_result[0]['geometry']['location']['lng']
        
        instance = Artisan.objects.create(**validated_data)
        types = request.data.get('types')
        for t in types:
            type_data=Type.objects.get(id=t)
            instance.type.add(type_data)
        return instance
    
    