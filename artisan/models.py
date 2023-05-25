from django.db import models
from karibu_backend.models import User

class Type(models.Model):
    name=models.CharField(max_length=255)

class Artisan(models.Model):
    name=models.CharField(max_length=255)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    address=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    website=models.CharField(max_length=255)
    zipcode=models.IntegerField
    city=models.CharField(max_length=255)
    longitude=models.CharField(max_length=255)
    latitude=models.CharField(max_length=255)
    type=models.ManyToManyField(Type)

    def __str__(self):
        return self.name
    
