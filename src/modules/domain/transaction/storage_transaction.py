from datetime import datetime

from src.modules.domain.base.abstract_reference import AbstractReference
from src.modules.domain.enum.storage_types import TransactionType
from src.modules.domain.measures.measurment_unit_model import MeasurementUnit
from src.modules.domain.nomenclature.nomenclature_model import Nomenclature
from src.modules.domain.storage.storage_model import Storage


class StorageTransaction(AbstractReference):

    __storage: Storage = None
    __nomenclature: Nomenclature = None
    __amount: float = 0.0
    __transaction_type: TransactionType = TransactionType.OUTGOING
    __measurement_unit: MeasurementUnit = None
    __transaction_time: datetime = None

    @classmethod
    def create(cls, storage: Storage=None, nomenclature: Nomenclature=None, amount: float=0.0, transaction_type: TransactionType=TransactionType.OUTGOING, measurement_unit: MeasurementUnit=None, time: datetime = None):
        instance = cls()
        instance.__storage = storage
        instance.__nomenclature = nomenclature
        instance.__transaction_type = transaction_type
        instance.__measurement_unit = measurement_unit
        instance.__transaction_time = time
        instance.__amount = amount
        return instance

    @property
    def storage(self) -> Storage:
        return self.__storage

    @storage.setter
    def storage(self, value: Storage):
        self.__storage = value

    @property
    def nomenclature(self) -> Nomenclature:
        return self.__nomenclature

    @nomenclature.setter
    def nomenclature(self, value: Nomenclature):
        self.__nomenclature = value

    @property
    def amount(self) -> float:
        return self.__amount

    @amount.setter
    def amount(self, value: float):
        self.__amount = value

    @property
    def transaction_type(self) -> int:
        return self.__transaction_type

    @transaction_type.setter
    def transaction_type(self, value: TransactionType):
        self.__transaction_type = value

    @property
    def measurement_unit(self) -> MeasurementUnit:
        return self.__measurement_unit

    @measurement_unit.setter
    def measurement_unit(self, value: MeasurementUnit):
        self.__measurement_unit = value

    @property
    def transaction_time(self) -> datetime:
        return self.__transaction_time

    @transaction_time.setter
    def transaction_time(self, value: datetime):
        self.__transaction_time = value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, StorageTransaction):
            return False
        return (self.__storage == other.__storage and
                self.__nomenclature == other.__nomenclature and
                self.__amount == other.__amount and
                self.__transaction_type == other.__transaction_type and
                self.__measurement_unit == other.__measurement_unit and
                self.__transaction_time == other.__transaction_time)

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)