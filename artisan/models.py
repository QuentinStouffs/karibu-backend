from django.db import models
from karibu_backend.models import User

TYPE_ARTISAN=(
    ("1", "Maraicher"),
    ("2", "Brasseur"),
    ("3", "Point de Vente"),
    ("4", "Vigneron"),
    ("5", "Boucher"),
    ("6", "Poissonnier"),
    ("7", "Epicier"),
    ("8", "Boulanger"),
    ("9", "Restaurant"),
    ("10", "Autre")
)

class Type(models.Model):
    name=models.CharField(max_length=30, choices=TYPE_ARTISAN, default="10")
    def __str__(self):
        return self.name
    
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
    
