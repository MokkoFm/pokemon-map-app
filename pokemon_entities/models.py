from django.db import models
from PIL import Image

class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name="название покемона на английском языке")
    image = models.ImageField(upload_to="pokemons", null=True, blank=True, verbose_name="изображение покемона")
    title_ru = models.CharField(max_length=200, verbose_name="название покемона на русском языке")
    title_jp = models.CharField(max_length=200, blank=True, verbose_name="название покемона на японском языке", default="")
    description = models.TextField(max_length=500, blank=True, verbose_name="описание покемона", default="Здесь будет описание покемона")
    previous_evolution = models.ForeignKey("self", blank=True, null=True, on_delete=models.CASCADE, default=None, related_name="next_evolution", verbose_name="предыдущая эволюция покемона")

    def __str__(self):
        return f"{self.title}"


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, default=None, verbose_name="покемон")
    lat = models.FloatField(default=0, blank=True, null=True, verbose_name="широта координат покемона")
    lon = models.FloatField(default=0, blank=True, null=True, verbose_name="долгота координат покемона")
    appeared_at = models.DateTimeField(default=None, blank=True, null=True, verbose_name="появление покемона")
    disappeared_at = models.DateTimeField(default=None, blank=True, null=True, verbose_name="исчезновение покемона")
    level = models.IntegerField(default=None, blank=True, null=True, verbose_name="уровень покемона")
    health = models.IntegerField(default=None, blank=True, null=True, verbose_name="здоровье покемона")
    strength = models.IntegerField(default=None, blank=True, null=True, verbose_name="сила покемона")
    defence = models.IntegerField(default=None, blank=True, null=True, verbose_name="защита покемона")
    stamina = models.IntegerField(default=None, blank=True, null=True, verbose_name="выносливость покемона")


    def __str__(self):
        return f"{self.pokemon.title} {self.lat} {self.lon}"