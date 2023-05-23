# Generated by Django 4.2 on 2023-05-23 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('1', 'Maraicher'), ('2', 'Brasseur'), ('3', 'Point de Vente'), ('4', 'Vigneron'), ('5', 'Boucher'), ('6', 'Poissonnier'), ('7', 'Epicier'), ('8', 'Boulanger'), ('9', 'Restaurant'), ('10', 'Autre')], default='10', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Artisan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('website', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('longitude', models.CharField(max_length=255)),
                ('latitude', models.CharField(max_length=255)),
                ('type', models.ManyToManyField(to='artisan.type')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
