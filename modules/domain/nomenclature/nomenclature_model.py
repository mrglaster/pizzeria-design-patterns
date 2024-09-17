from modules.domain.base.abstract_reference import AbstractReference
from modules.domain.measures.measurment_unit_model import MeasurementUnit
from modules.domain.nomenclature.nomenclature_group_model import NomenclatureGroup
from modules.service.util.validation.data_validator import DataValidator


class Nomenclature(AbstractReference):
    __full_name: str = None
    __nomenclature_group: NomenclatureGroup = None
    __measurement_unit: MeasurementUnit = None
    __full_name_property_name = "nomenclature_full_name"

    def __init__(self, name: str, nomenclature_group: NomenclatureGroup, measurement_unit: MeasurementUnit,
                 full_name: str = None):
        super().__init__(name, self.__full_name_property_name)
        DataValidator.validate_field_type(nomenclature_group, NomenclatureGroup)
        DataValidator.validate_field_type(measurement_unit, MeasurementUnit)
        DataValidator.check_class_field(self.__full_name_property_name, str, full_name)
        self.__nomenclature_group = nomenclature_group
        self.__measurement_unit = measurement_unit
        self.__full_name = full_name

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value: str):
        DataValidator.check_class_field(self.__full_name_property_name, str, value)
        self.__full_name = value

    @property
    def measurement_unit(self):
        return self.__measurement_unit

    @measurement_unit.setter
    def measurement_unit(self, value: MeasurementUnit):
        DataValidator.validate_field_type(value, MeasurementUnit)
        self.__measurement_unit = value

    @property
    def nomenclature_group(self):
        return self.__nomenclature_group

    @nomenclature_group.setter
    def nomenclature_group(self, value: NomenclatureGroup):
        DataValidator.validate_field_type(value, NomenclatureGroup)
        self.__nomenclature_group = value

    def __eq__(self, other):
        if not isinstance(other, Nomenclature):
            return False
        return self._name == other._name

    def __ne__(self, other):
        return not self == other
