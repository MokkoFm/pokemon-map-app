import folium
import json
import sys
import os

from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import Pokemon
from .models import PokemonEntity
from django.shortcuts import get_object_or_404



MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832&fill=transparent"


def add_pokemon(folium_map, lat, lon, name, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        tooltip=name,
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemons = Pokemon.objects.all()
    pokemons_on_page = []

    for pokemon in pokemons:
        locations = PokemonEntity.objects.filter(pokemon=pokemon)

        if pokemon.image:
            image_url = pokemon.image.url

        for location in locations:
            add_pokemon(folium_map, location.lat, location.lon, pokemon.title, request.build_absolute_uri(image_url))
        
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': image_url,
            'title_ru': pokemon.title_ru,
        })

    return render(request, "mainpage.html", context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemons = Pokemon.objects.filter(id=pokemon_id)
    for pokemon in pokemons:
        if pokemon.image:
            image_url = pokemon.image.url

        locations = PokemonEntity.objects.filter(pokemon=pokemon)
        for location in locations:
            add_pokemon(folium_map, location.lat, location.lon, pokemon.title, request.build_absolute_uri(image_url))

        requested_pokemon = {
                'pokemon_id': pokemon.id, 
                'title_en': pokemon.title, 
                'img_url': image_url, 
                'title_ru': pokemon.title_ru, 
                'title_jp': pokemon.title_jp, 
                'description': pokemon.description
            }

        if pokemon.previous_evolution:
            previous_pokemon = {
                'pokemon_id': pokemon.previous_evolution.id,
                'title_ru':  pokemon.previous_evolution.title_ru,
                'img_url': pokemon.previous_evolution.image.url
            }

            requested_pokemon['previous_evolution'] = previous_pokemon

        if pokemon.next_evolution:
            current_pokemon = Pokemon.objects.get(id=pokemon_id)
            next_evolutions = current_pokemon.next_evolution.all()
            for next_evolution in next_evolutions:
                next_pokemon = {
                    'pokemon_id': next_evolution.id,
                    'title_ru':  next_evolution.title_ru,
                    'img_url': next_evolution.image.url
                }
                    
                requested_pokemon['next_evolution'] = next_pokemon

    return render(request, "pokemon.html", context={'map': folium_map._repr_html_(),
                                                    'pokemon': requested_pokemon})
