from abc import ABC


class AbstractProcess(ABC):

    @staticmethod
    def calculate(data: list, add_to_repository: bool = False, *kwargs):
        pass
