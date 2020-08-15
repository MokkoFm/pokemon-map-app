# Generated by Django 2.2.3 on 2020-08-12 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0009_auto_20200812_1934'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='latitude',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='longitude',
            new_name='lon',
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.Pokemon'),
        ),
    ]