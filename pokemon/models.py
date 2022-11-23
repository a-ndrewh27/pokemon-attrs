import random


class Pokemon:
  def __init__(self, id: int, name: str, height: int, weight: int, moves: list[any], color: str, base_happiness: int):
    self.id = id
    self.name = name
    self.height = height
    self.weight = weight
    self.moves = [m["move"]["name"] for m in random.sample(
        moves, 2)] if len(moves) > 1 else [moves[0]["move"]["name"]]
    self.color = color
    self.base_happiness = base_happiness

  @staticmethod
  def from_json(base_json: dict, species_json: dict):
    return Pokemon(base_json["id"],
                   base_json["name"],
                   base_json["height"],
                   base_json["weight"],
                   base_json["moves"],
                   species_json["color"]["name"],
                   species_json["base_happiness"])
