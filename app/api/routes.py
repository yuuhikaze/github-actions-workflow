from fastapi import APIRouter

from app.calculator import sum, sub, multiply
from app.schemas.dto import OperationRequest, OperationResponse

router = APIRouter()


@router.post("/add", response_model=OperationResponse, status_code=200)
def add(body: OperationRequest):
    result = sum(body.a, body.b)
    return OperationResponse(result=result, operation="add")


@router.post("/subtract", response_model=OperationResponse, status_code=200)
def subtract(body: OperationRequest):
    result = sub(body.a, body.b)
    return OperationResponse(result=result, operation="subtract")


@router.post("/multiply", response_model=OperationResponse, status_code=200)
def multiply_op(body: OperationRequest):
    result = multiply(body.a, body.b)
    return OperationResponse(result=result, operation="multiply")
