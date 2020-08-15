# Generated by Django 2.2.3 on 2020-08-12 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0004_pokemonentity'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonentity',
            name='latitude',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='longitude',
            field=models.FloatField(default=0),
        ),
    ]
