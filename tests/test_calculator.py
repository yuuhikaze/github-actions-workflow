from fastapi.testclient import TestClient

from app.calculator import sum, sub, multiply
from app.main import app

client = TestClient(app)


def test_sum() -> None:
    assert sum(2, 3) == 5


def test_sub() -> None:
    assert sub(5, 3) == 2


def test_multiply() -> None:
    assert multiply(2, 3) == 6


def test_add_endpoint() -> None:
    response = client.post("/add", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 5, "operation": "add"}


def test_subtract_endpoint() -> None:
    response = client.post("/subtract", json={"a": 5, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 2, "operation": "subtract"}


def test_multiply_endpoint() -> None:
    response = client.post("/multiply", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 6, "operation": "multiply"}
