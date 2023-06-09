from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import status
from .ArtisanSerializer import *
from .models import Artisan
import sys

@api_view(['GET', 'POST'])
@permission_classes([])
@authentication_classes([])
def artisans_list(request):
    if request.method == 'GET':
        artisans = Artisan.objects.all()

        serializer = ArtisanSerializer(artisans, context={'request': request}, many=True)

        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArtisanSerializerWOLatLon(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def artisan_by_user(request, user): 
    artisans = Artisan.objects.all().filter(user=user)
    serializer = ArtisanSerializer(artisans, context={'request': request}, many=True)
    return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
def artisan_details(request, id):
    try:
        artisan = Artisan.objects.get(id=id)
    except Artisan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ArtisanSerializerWOLatLon(artisan, data=request.data,context={'request': request})
    
        if serializer.is_valid():
            serializer.save()
            types = []
            for t in request.data.get('types'): 
                try:
                   type = Type.objects.get(id=t)
                   types.append(type)
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)
            artisan.type.set(types) 
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET': 
        serializer=ArtisanSerializer(artisan,context={'request': request}, many=True)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        artisan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def artisan_detail(request, id):
    try:
        artisan = Artisan.objects.get(id=id)
    except Artisan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer=ArtisanSerializer(artisan,context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def get_artisans_by_radius(request, lat, long, radius):
    try:
        artisans=Artisan.objects.raw(
            """
            SELECT * from artisan_artisan
            WHERE
              ST_Distance_Sphere(
                POINT(%s, %s),
                POINT(longitude, latitude)
                ) < %s ;
            """, [long, lat, radius])
    except Artisan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ArtisanSerializer(artisans, context={'request': request}, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def get_artisans_by_address(request, radius):
    address = request.GET.get('address','')

    gmaps=googlemaps.Client(key='Google_api_key')
    geocode_result=gmaps.geocode(address)
    lat=geocode_result[0]['geometry']['location']['lat']
    long=geocode_result[0]['geometry']['location']['lng']
    try:
        artisans=Artisan.objects.raw(
            """
            SELECT * from artisan_artisan
            WHERE
              ST_Distance_Sphere(
                POINT(%s, %s),
                POINT(longitude, latitude)
                ) < %s ;
            """, [long, lat, radius])
    except Artisan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ArtisanSerializer(artisans, context={'request': request}, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def types(request):
    types = Type.objects.all()
    serializer = TypeSerializer(types,  context={'request': request}, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def geo(request): 
    full_address=request.GET.get('address', '')
    print("the address:" + full_address, file=sys.stderr)
    gmaps=googlemaps.Client(key='Google_api_key')
    geocode_result=gmaps.geocode(full_address)
    geo = {
        "lat" : geocode_result[0]['geometry']['location']['lat'],
        "lng" : geocode_result[0]['geometry']['location']['lng']
    }
    
    return JsonResponse(geo)
