class DomainError(Exception):
    """Base exception for domain layer"""
    pass


class ValidationError(DomainError):
    pass
