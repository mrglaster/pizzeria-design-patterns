from abc import ABC, abstractmethod

from src.modules.validation.data_validator import DataValidator


class AbstractPrototype(ABC):
    __data = []

    def __init__(self, source: list):
        super().__init__()
        DataValidator.validate_field_type(source, list)
        self.__data = source

    @abstractmethod
    def create(self, data: list, filter):
        DataValidator.validate_field_type(data, list)

        # instance = AbstractPrototype(data)
        # return instance

    @property
    def data(self) -> list:
        return self.__data

    @data.setter
    def data(self, value: list):
        self.__data = value
