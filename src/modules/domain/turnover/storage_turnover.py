from src.modules.domain.base.abstract_reference import AbstractReference
from src.modules.domain.measures.measurment_unit_model import MeasurementUnit
from src.modules.domain.nomenclature.nomenclature_model import Nomenclature
from src.modules.domain.storage.storage_model import Storage


class StorageTurnover(AbstractReference):
    __storage: Storage = None
    __turnover: float = 0.0
    __nomenclature: Nomenclature = None
    __measurement_unit: MeasurementUnit = None

    @classmethod
    def create(cls, storage: Storage = None, turnover: float = 0.0, nomenclature: Nomenclature = None,
               measurement_unit: MeasurementUnit = None):
        instance = cls()
        instance.storage = storage
        instance.turnover = turnover
        instance.nomenclature = nomenclature
        instance.measurement_unt = measurement_unit
        return instance

    @property
    def storage(self):
        return self.__storage

    @storage.setter
    def storage(self, other):
        self.__storage = other

    @property
    def turnover(self):
        return self.__turnover

    @turnover.setter
    def turnover(self, other):
        self.__turnover = other

    @property
    def nomenclature(self):
        return self.__nomenclature

    @nomenclature.setter
    def nomenclature(self, other):
        self.__nomenclature = other

    @property
    def measurement_unit(self):
        return self.__measurement_unit

    @measurement_unit.setter
    def measurement_unit(self, other):
        self.__measurement_unit = other

    def __eq__(self, other):
        return self.nomenclature == other.nomenclature and self.turnover == other.turnover and self.measurement_unit == other.measurement_unit and self.storage == other.storage

    def __ne__(self, other):
        return self != other
