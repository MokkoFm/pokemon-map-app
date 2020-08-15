# Generated by Django 2.2.3 on 2020-08-15 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0016_auto_20200815_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.TextField(blank=True, default='Здесь будет описание покемона', max_length=500, verbose_name='описание покемона'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='pokemons', verbose_name='изображение покемона'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='previous_evolution',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='next_evolution', to='pokemon_entities.Pokemon', verbose_name='предыдущая эволюция покемона'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title',
            field=models.CharField(max_length=200, verbose_name='название покемона на английском языке'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='название покемона на японском языке'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_ru',
            field=models.CharField(default='', max_length=200, verbose_name='название покемона на русском языке'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='появление покемона'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='defence',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='защита покемона'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='исчезновение покемона'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='health',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='здоровье покемона'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='lat',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='широта координат покемона'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='level',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='уровень покемона'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='lon',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='долгота координат покемона'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.Pokemon', verbose_name='покемон'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='stamina',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='выносливость покемона'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='strength',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='сила покемона'),
        ),
    ]
