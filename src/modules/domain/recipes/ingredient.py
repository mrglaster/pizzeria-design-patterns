from src.modules.domain.base.abstract_reference import AbstractReference
from src.modules.domain.nomenclature.nomenclature_model import Nomenclature
from src.modules.domain.measures.measurment_unit_model import MeasurementUnit
from src.modules.validation.data_validator import DataValidator


class Ingredient(AbstractReference):
    def __init__(self, nomenclature: Nomenclature, measurement_unit: MeasurementUnit, amount: float):
        super().__init__()
        DataValidator.validate_field_type(nomenclature, Nomenclature)
        DataValidator.validate_field_type(measurement_unit, MeasurementUnit)
        DataValidator.validate_field_type(amount, float)
        self.__nomenclature = nomenclature
        self.__amount = amount

    @property
    def nomenclature(self):
        return self.__nomenclature

    @nomenclature.setter
    def nomenclature(self, value: Nomenclature):
        DataValidator.validate_field_type(value, Nomenclature)
        self.__nomenclature = value

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value: float):
        DataValidator.validate_field_type(value, float)
        self.__amount = value

    def __eq__(self, other):
        if not isinstance(other, Ingredient):
            return False
        return (
                self.__nomenclature == other.nomenclature and
                self.__amount == other.amount
        )

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return f"{self.__nomenclature.name} - {self.amount} {self.__nomenclature.measurement_unit.name}"