from pydantic import BaseModel, Field


class OperationRequest(BaseModel):
    a: int = Field(description="First operand")
    b: int = Field(description="Second operand")


class OperationResponse(BaseModel):
    result: int
    operation: str
