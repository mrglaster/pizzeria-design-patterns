from __future__ import annotations
from src.modules.domain.base.abstract_reference import AbstractReference
from src.modules.validation.data_validator import DataValidator


class MeasurementUnit(AbstractReference):
    __unit: float = 0
    __base_measurement_unit: MeasurementUnit = None

    def __init__(self, name: str = "DEFAULT"):
        super().__init__(name)

    @classmethod
    def create(cls, name: str = "DEFAULT", unit: float = 0.0,
               base_measure_unit: MeasurementUnit = None) -> MeasurementUnit:
        unit = cls.__convert_to_float(unit)
        DataValidator.validate_field_type(unit, float)
        DataValidator.validate_field_type(base_measure_unit, MeasurementUnit, True)

        instance = cls(name)
        instance.__unit = unit
        instance.__base_measurement_unit = base_measure_unit
        return instance

    @property
    def unit(self):
        return self.__unit

    @property
    def base_measure_unit(self):
        return self.__base_measurement_unit

    @unit.setter
    def unit(self, value: float):
        DataValidator.validate_field_type(float(value), float)
        value = self.__convert_to_float(value)
        self.__unit = value

    @base_measure_unit.setter
    def base_measure_unit(self, value: MeasurementUnit):
        DataValidator.validate_field_type(value, MeasurementUnit, nullable=True)
        self.__base_measurement_unit = value

    def __eq__(self, other):
        if not isinstance(other, MeasurementUnit):
            return False
        return self._name == other._name

    def __ne__(self, other):
        if not isinstance(other, MeasurementUnit):
            return True
        return self._name != other._name

    @staticmethod
    def __convert_to_float(unit: (int | float)):
        if isinstance(unit, int):
            unit = float(unit)
        return unit

    def __str__(self):
        if self.base_measure_unit is not None:
            return f"{self.name}: ({self.base_measure_unit.name} {self.unit})"
        return f"{self.name}: 1"
