import requests
from flask import abort
from .models import Pokemon

API_URL = "https://pokeapi.co/api/v2/pokemon/"


class PokemonService:
  def get_by_id(pokemon_id: int):

    data = requests.get(API_URL + str(pokemon_id))
    if data.status_code == 404:
      abort(404, "Pokemon not found")

    data_as_json = data.json()
    species_url = data_as_json["species"]["url"]
    species_data = requests.get(species_url)
    species_data_as_json = species_data.json()

    pokemon = Pokemon.from_json(data_as_json, species_data_as_json)
    return pokemon
