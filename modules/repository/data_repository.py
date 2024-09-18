from modules.service.base.abstract_logic import AbstractLogic


class DataRepository(AbstractLogic):
    __data = []

    @staticmethod
    def group_key() -> str:
        return "group"

    @property
    def data(self):
        return self.__data

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(DataRepository, cls).__new__(cls)
        return cls.instance
