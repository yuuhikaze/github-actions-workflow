from __future__ import annotations
from dataclasses import dataclass, field
from uuid import uuid4

from app.domain.exceptions import ValidationError


@dataclass
class Operation:
    a: int
    b: int
    operation_type: str
    result: int = field(init=False)
    id: str = field(default_factory=lambda: str(uuid4()))

    def __post_init__(self) -> None:
        if self.operation_type not in ("add", "subtract", "multiply"):
            raise ValidationError(
                "operation_type must be 'add', 'subtract', or 'multiply'"
            )
        self._compute_result()

    def _compute_result(self) -> None:
        if self.operation_type == "add":
            self.result = self.a + self.b
        elif self.operation_type == "subtract":
            self.result = self.a - self.b
        elif self.operation_type == "multiply":
            self.result = self.a * self.b
