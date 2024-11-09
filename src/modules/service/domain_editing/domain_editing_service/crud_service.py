from abc import ABC

from src.modules.domain.base.abstract_reference import AbstractReference


class AbstractCrudService(ABC):

    @staticmethod
    def create(obj: AbstractReference):
        pass

    @staticmethod
    def read(uid: str) -> AbstractReference:
        pass

    @staticmethod
    def update(uid: str, new_object: AbstractReference) -> bool:
        pass

    @staticmethod
    def delete(uid: str) -> bool:
        pass