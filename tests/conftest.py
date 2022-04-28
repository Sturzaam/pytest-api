import pytest
from starlette.testclient import TestClient

from test_app.main import app


@pytest.fixture
def client():
    yield TestClient(app)
