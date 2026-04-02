from __future__ import annotations
from typing import Protocol

from app.domain.entities import Operation


class OperationRepository(Protocol):
    def add(self, operation: Operation) -> None:
        ...

    def get(self, operation_id: str) -> Operation:
        ...

    def list(self) -> list[Operation]:
        ...
