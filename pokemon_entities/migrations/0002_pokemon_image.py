# Generated by Django 2.2.3 on 2020-08-12 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(null=True, upload_to='pokemons'),
        ),
    ]
