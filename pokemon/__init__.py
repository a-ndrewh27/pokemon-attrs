BASE_ROUTE = "pokemon"


def register_routes(api, root="api"):
  from .controller import api as pokemon_api

  api.add_namespace(pokemon_api, path=f"/{root}/{BASE_ROUTE}")
