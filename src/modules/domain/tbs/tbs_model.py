from __future__ import annotations
from src.modules.domain.base.abstract_reference import AbstractReference
from src.modules.validation.data_validator import DataValidator


class Tbs(AbstractReference):
    __opening_remainder: list = []
    __receipt: list = []
    __consumption: list = []
    __remainder: list = []

    @staticmethod
    def create(opening_remainder: list, receipt: list, consumption: list, remainder: list, name: str = ""):
        instance = Tbs()
        instance.opening_remainder = opening_remainder
        instance.receipt = receipt
        instance.consumption = consumption
        instance.remainder = remainder
        instance.name = name
        return instance

    @property
    def opening_remainder(self) -> list:
        return self.__opening_remainder

    @opening_remainder.setter
    def opening_remainder(self, opening_remainder: list):
        DataValidator.validate_field_type(opening_remainder, list)
        self.__opening_remainder = opening_remainder

    @property
    def receipt(self) -> list:
        return self.__receipt

    @receipt.setter
    def receipt(self, receipt: list):
        DataValidator.validate_field_type(receipt, list)
        self.__receipt = receipt

    @property
    def consumption(self) -> list:
        return self.__consumption

    @consumption.setter
    def consumption(self, consumption: list):
        DataValidator.validate_field_type(consumption, list)
        self.__consumption = consumption

    @property
    def remainder(self) -> list:
        return self.__remainder

    @remainder.setter
    def remainder(self, remainder: list):
        DataValidator.validate_field_type(remainder, list)
        self.__remainder = remainder

    def __eq__(self, other: Tbs):
        if not isinstance(other, Tbs):
            return False
        return self.receipt == other.receipt and self.remainder == other.remainder and self.name == other.name and self.consumption == other.consumption and self.opening_remainder == other.opening_remainder

    def __ne__(self, other: Tbs):
        if not isinstance(other, Tbs):
            return False
        return not self == other
