from app.domain.entities import Operation
from app.domain.exceptions import ValidationError


class MemoryOperationRepository:
    def __init__(self) -> None:
        self._operations: dict[str, Operation] = {}

    def add(self, operation: Operation) -> None:
        self._operations[operation.id] = operation

    def get(self, operation_id: str) -> Operation:
        if operation_id not in self._operations:
            raise ValidationError(f"Operation with id {operation_id} not found")
        return self._operations[operation_id]

    def list(self) -> list[Operation]:
        return list(self._operations.values())
