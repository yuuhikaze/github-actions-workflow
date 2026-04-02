from fastapi.testclient import TestClient

from app.calculator import sum, sub, multiply
from app.main import app
from app.domain.entities import Operation
from app.repositories.memory import MemoryOperationRepository
from app.services.calculator_service import CalculatorService

client = TestClient(app)


def test_sum() -> None:
    assert sum(2, 3) == 5


def test_sub() -> None:
    assert sub(5, 3) == 2


def test_multiply() -> None:
    assert multiply(2, 3) == 6


def test_operation_entity_add() -> None:
    op = Operation(a=2, b=3, operation_type="add")
    assert op.result == 5
    assert op.operation_type == "add"


def test_operation_entity_subtract() -> None:
    op = Operation(a=5, b=3, operation_type="subtract")
    assert op.result == 2
    assert op.operation_type == "subtract"


def test_operation_entity_multiply() -> None:
    op = Operation(a=2, b=3, operation_type="multiply")
    assert op.result == 6
    assert op.operation_type == "multiply"


def test_memory_repository_add() -> None:
    repo = MemoryOperationRepository()
    op = Operation(a=2, b=3, operation_type="add")
    repo.add(op)
    retrieved = repo.get(op.id)
    assert retrieved.result == 5


def test_calculator_service() -> None:
    repo = MemoryOperationRepository()
    service = CalculatorService(repo)
    op = service.execute(2, 3, "add")
    assert op.result == 5
    assert len(service.list_operations()) == 1


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
