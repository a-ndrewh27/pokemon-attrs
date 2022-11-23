import pytest
import json


@pytest.mark.asyncio
async def test_get_pokemon_by_id(client):
  pokemon_id = 132
  path = f"api/pokemon/id/{pokemon_id}"
  response = client.get(path)

  assert response.status_code == 200

  data = json.loads(response.data.decode("utf8"))
  assert data["name"] == "ditto"
  assert data["weight"] == 40
  assert data["color"] == "purple"
  assert data["id"] == pokemon_id
  assert data["base_happiness"] == 50


@pytest.mark.asyncio
async def test_get_top_five(client):
  path = f"api/pokemon/top-five"
  response = client.get(path)

  assert response.status_code == 200

  data = json.loads(response.data.decode("utf8"))

  assert len(data["top_five"]) == 5
  assert data["team_base_happiness"]["average"] == 37
  assert data["team_base_happiness"]["median"] == 50
