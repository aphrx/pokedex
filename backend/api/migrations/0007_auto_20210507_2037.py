# Generated by Django 3.2 on 2021-05-08 03:37

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_pokemon_national_dex'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='desc',
            field=models.CharField(default=api.models.default_value, max_length=1024),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='type1',
            field=models.CharField(default=api.models.default_value, max_length=255),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='type2',
            field=models.CharField(default=api.models.default_value, max_length=255),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='pokemonimagesearch',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
