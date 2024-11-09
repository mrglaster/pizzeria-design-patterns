from src.modules.service.base.abstract_logic import AbstractLogic


class AbstractRepository(AbstractLogic):

    def set_exception(self, ex: Exception):
        pass

    @staticmethod
    def find_by_name(name: str):
        pass

    @staticmethod
    def clear():
       pass

    @staticmethod
    def get_all():
        pass

    @staticmethod
    def add(obj):
        pass

    @staticmethod
    def delete(obj):
        pass

    @staticmethod
    def update(old_object, new_object):
        pass