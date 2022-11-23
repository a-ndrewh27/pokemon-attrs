import pytest

from app import create_app


@pytest.fixture
def client():
  test_app = create_app("test")

  yield test_app.test_client()
