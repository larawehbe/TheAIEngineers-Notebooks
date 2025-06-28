import pytest
from fastapi.testclient import TestClient
from main import app  # Adjust if your main.py is nested

@pytest.fixture(scope="module")
def test_client():
    return TestClient(app)
