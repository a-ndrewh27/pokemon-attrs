from pokemon.models import Pokemon


def test_new_pokemon():
  """
  GIVEN a Pokemon model
  WHEN a new Pokemon is created
  THEN check attributes name, height, weight, moves, color, base_happiness
  """
  pokemon = Pokemon(1,
                    "bulbasaur",
                    7,
                    69,
                    [{"move": {"name": "grass-pledge"}}, {"move": {"name": "razor-wind"}}, {"move": {"name": "swords-dance"}}, {
                        "move": {"name": "cut"}}, {"move": {"name": "bind"}}, {"move": {"name": "skull-bash"}}, {"move": {"name": "outrage"}}],
                    "green",
                    50)

  assert pokemon.name == 'bulbasaur'
  assert pokemon.height == 7
  assert pokemon.weight == 69
  assert len(pokemon.moves) == 2
  assert pokemon.color == 'green'
  assert pokemon.base_happiness == 50


def test_new_pokemon_from_json():
  """
  GIVEN pokemon data via two dictionaries
  WHEN a new pokemon is created from json
  THEN check attributes 
  """

  pokemon = Pokemon.from_json(
      {
          "id": 1, "name": "bulbasaur", "height": 7, "weight": 69, "moves": [{"move": {"name": "grass-pledge"}}, {"move": {"name": "razor-wind"}}, {"move": {"name": "swords-dance"}}, {"move": {"name": "cut"}}, {"move": {"name": "bind"}}, {"move": {"name": "skull-bash"}}, {"move": {"name": "outrage"}}]
      },
      {
          "color": {"name": "green"}, "base_happiness": 50
      })

  assert pokemon.name == 'bulbasaur'
  assert pokemon.height == 7
  assert pokemon.weight == 69
  assert len(pokemon.moves) == 2
  assert pokemon.color == 'green'
  assert pokemon.base_happiness == 50
