# Generated by Django 2.2.16 on 2021-05-06 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_pokemon_national_dex'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='national_dex',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
    ]