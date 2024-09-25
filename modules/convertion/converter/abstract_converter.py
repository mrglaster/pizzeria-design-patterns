from abc import ABC

from modules.service.base.abstract_logic import AbstractLogic


class AbstractConverter(AbstractLogic):

    def set_exception(self, ex: Exception):
        pass

    @staticmethod
    def convert(obj: object) -> str:
        pass
