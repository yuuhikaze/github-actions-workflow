from app.domain.entities import Operation
from app.repositories.base import OperationRepository


class CalculatorService:
    def __init__(self, repo: OperationRepository) -> None:
        self.repo = repo

    def execute(self, a: int, b: int, operation_type: str) -> Operation:
        operation = Operation(a=a, b=b, operation_type=operation_type)
        self.repo.add(operation)
        return operation

    def get_operation(self, operation_id: str) -> Operation:
        return self.repo.get(operation_id)

    def list_operations(self) -> list[Operation]:
        return self.repo.list()
