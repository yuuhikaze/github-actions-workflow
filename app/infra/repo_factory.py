from app.repositories.memory import MemoryOperationRepository


class RepositoryFactory:
    @staticmethod
    def create_operation_repo():
        return MemoryOperationRepository()
