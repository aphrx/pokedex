# Generated by Django 2.2.16 on 2021-05-03 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20210503_2223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='evolution_id',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='preevolution_id',
        ),
    ]
