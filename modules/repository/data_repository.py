from modules.service.base.abstract_logic import AbstractLogic


class AbstractRepository(AbstractLogic):

    def set_exception(self, ex: Exception):
        pass

    @staticmethod
    def clear():
       pass

    @staticmethod
    def get_all():
        pass
