from src.modules.domain.enum.storage_types import TransactionType
from src.modules.domain.turnover.storage_turnover import StorageTurnover
from src.modules.service.process.abstract import AbstractProcess


class StorageTurnoverProcess(AbstractProcess):

    @staticmethod
    def calculate(transactions: list) -> list:
        result = {}
        dt = []
        for transaction in transactions:
            storage = transaction.storage
            nomenclature = transaction.nomenclature
            measurement_unit = transaction.measurement_unit

            info_tuple = (storage, nomenclature, measurement_unit)
            if info_tuple not in dt:
                dt.append(info_tuple)
            key = dt.index(info_tuple)

            value = transaction.amount
            if transaction.transaction_type == TransactionType.OUTGOING:
                value = -value
            result[key] = result.get(key, 0) + value
        turns = []
        for key, value in result.items():
            key_data = dt[key]
            turn = StorageTurnover.create(storage=key_data[0], turnover=value, nomenclature=key_data[1],
                                          measurement_unit=key_data[2])
            turns.append(turn)
        return turns
