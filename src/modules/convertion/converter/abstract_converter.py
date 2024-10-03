from abc import ABC

from src.modules.factory.model_description_factory.model_description_factory import ModelDescriptionFactory
from src.modules.service.base.abstract_logic import AbstractLogic


class AbstractConverter(AbstractLogic):
    objects_factory = ModelDescriptionFactory()

    def set_exception(self, ex: Exception):
        pass

    @staticmethod
    def serialize(obj: object) -> str:
        pass

    @staticmethod
    def deserialize(object_name: str, data: dict|str) -> object:
        pass
