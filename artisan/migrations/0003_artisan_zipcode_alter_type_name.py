# Generated by Django 4.2 on 2023-05-27 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artisan', '0002_auto_20230524_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='artisan',
            name='zipcode',
            field=models.IntegerField(default=5030),
        ),
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
