# Generated by Django 3.2 on 2021-05-08 03:39

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210507_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type2',
            field=models.CharField(default=api.models.default_value, max_length=255, null=True),
        ),
    ]