from __future__ import annotations
from modules.domain.base.abstract_reference import AbstractReference
from modules.validation.data_validator import DataValidator


class MeasurementUnit(AbstractReference):
    __unit: float = 0
    __base_measure_unit: MeasurementUnit = None

    def __init__(self, name: str, unit: float, base_measure_unit: MeasurementUnit = None):
        super().__init__(name, )
        unit = self.__convert_to_float(unit)
        DataValidator.validate_field_type(unit, float)
        DataValidator.validate_field_type(base_measure_unit, MeasurementUnit, True)
        self.__unit = unit
        self.__base_measure_unit = base_measure_unit

    @property
    def unit(self):
        return self.__unit

    @property
    def base_measure_unit(self):
        return self.__base_measure_unit

    @unit.setter
    def unit(self, value: float):
        DataValidator.validate_field_type(float(value),  float)
        value = self.__convert_to_float(value)
        self.__unit = value

    @base_measure_unit.setter
    def base_measure_unit(self, value: MeasurementUnit):
        DataValidator.validate_field_type(value, MeasurementUnit)
        self.__base_measure_unit = value

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