from abc import ABC, abstractmethod


class AbstractProcess(ABC):

    @staticmethod
    def calculate(transactions: list) -> list:
        pass