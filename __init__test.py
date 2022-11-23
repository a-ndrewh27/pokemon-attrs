from test.conftest import client


def test_app_creates(client):
  assert client
