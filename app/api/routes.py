from fastapi import APIRouter, Depends, HTTPException

from app.infra.repo_factory import RepositoryFactory
from app.domain.exceptions import DomainError, ValidationError
from app.services.calculator_service import CalculatorService
from app.schemas.dto import OperationRequest, OperationResponse

router = APIRouter()

factory = RepositoryFactory()
operation_repo = factory.create_operation_repo()


def get_calculator_service() -> CalculatorService:
    return CalculatorService(operation_repo)


def to_http(e: Exception) -> HTTPException:
    if isinstance(e, (ValidationError, ValueError)):
        return HTTPException(status_code=400, detail=str(e))
    if isinstance(e, DomainError):
        return HTTPException(status_code=500, detail="Internal Server Error")
    return HTTPException(status_code=500, detail="Internal Server Error")


@router.post("/add", response_model=OperationResponse, status_code=200)
def add(
    body: OperationRequest, service: CalculatorService = Depends(get_calculator_service)
):
    try:
        operation = service.execute(body.a, body.b, "add")
        return OperationResponse(result=operation.result, operation="add")
    except Exception as e:
        raise to_http(e)


@router.post("/subtract", response_model=OperationResponse, status_code=200)
def subtract(
    body: OperationRequest, service: CalculatorService = Depends(get_calculator_service)
):
    try:
        operation = service.execute(body.a, body.b, "subtract")
        return OperationResponse(result=operation.result, operation="subtract")
    except Exception as e:
        raise to_http(e)


@router.post("/multiply", response_model=OperationResponse, status_code=200)
def multiply_op(
    body: OperationRequest, service: CalculatorService = Depends(get_calculator_service)
):
    try:
        operation = service.execute(body.a, body.b, "multiply")
        return OperationResponse(result=operation.result, operation="multiply")
    except Exception as e:
        raise to_http(e)
