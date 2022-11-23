import statistics
from flask_restx import Namespace, Resource
from flask import jsonify
from .service import PokemonService

api = Namespace("Pokemon")

TOP_FIVE_POKEMON_IDS = [6, 54, 149, 150, 80]


@api.route("/id/<int:pokemon_id>")
@api.param("pokemon_id", "Pokemon id number")
class PokemonIdResource(Resource):
  def get(self, pokemon_id: int):
    """Get Single Pokemon By id number"""

    pokemon = PokemonService.get_by_id(pokemon_id)
    return jsonify(pokemon.__dict__)


@api.route("/top-five")
class PokemonIdResource(Resource):
  def get(self):
    """Get top five favorite Pokemon"""

    poke_list = []

    for i in TOP_FIVE_POKEMON_IDS:
      pokemon = PokemonService.get_by_id(i)
      poke_list.append(pokemon)

    happiness_list = [p.base_happiness for p in poke_list]

    resp = {
        "top_five": [p.__dict__ for p in poke_list],
        "team_base_happiness": {
            "average": statistics.mean(happiness_list),
            "median": statistics.median(happiness_list)
        }
    }
    return jsonify(resp)
