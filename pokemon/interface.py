from mypy_extensions import TypedDict


class PokemonInterface(TypedDict, total=False):
  id: int
  name: str
  height: int
  weight: int
  color: str
  base_happiness: int
