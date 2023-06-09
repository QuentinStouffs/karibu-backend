# Generated by Django 4.2 on 2023-05-24 15:49

from django.db import migrations, models

TYPE_ARTISAN=(
    ("Maraicher"),
    ("Brasseur"),
    ("Point de Vente"),
    ("Vigneron"),
    ("Boucher"),
    ("Poissonnier"),
    ("Epicier"),
    ("Boulanger"),
    ("Restaurant"),
    ("Autre")
)

def add_types(apps, schema_editor):
    Type=apps.get_model('artisan', 'Type')
    for name in TYPE_ARTISAN:
        type=Type(name=name)
        type.save()


class Migration(migrations.Migration):

    dependencies = [
        ('artisan', '0001_initial'),
    ]

   
    operations = [
        migrations.RunPython(add_types),
    ]
