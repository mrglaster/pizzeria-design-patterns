from datetime import datetime
from src.modules.domain.enum.storage_types import TransactionType
from src.modules.domain.measures.measurment_unit_model import MeasurementUnit
from src.modules.domain.nomenclature.nomenclature_model import Nomenclature
from src.modules.domain.storage.storage_model import Storage
from src.modules.domain.transaction.storage_transaction import StorageTransaction
from src.modules.repository.data_repository import AbstractRepository
from src.modules.repository.storage_repository import StorageRepository
from src.modules.service.data_loader.storage_transactions_data_loader import StorageTransactionsDataLoader


class StorageTransactionRepository(AbstractRepository):
    __storage_transactions = {}

    @staticmethod
    def create_transaction(storage: Storage, nomenclature: Nomenclature, amount: float,
                           transaction_type: TransactionType, measurement_unit: MeasurementUnit,
                           time: datetime) -> 'StorageTransaction':
        transaction = StorageTransaction.create(
            storage=storage,
            nomenclature=nomenclature,
            amount=amount,
            transaction_type=transaction_type,
            measurement_unit=measurement_unit,
            time=time
        )
        key = f"{nomenclature.name}_{amount}_{transaction_type}_{time}"
        StorageTransactionRepository.__storage_transactions[key] = transaction
        return transaction

    @staticmethod
    def add(transaction_obj: StorageTransaction):
        key = f"{transaction_obj.nomenclature.name}_{transaction_obj.amount}_{transaction_obj.transaction_type}_{transaction_obj.transaction_time}"
        if key not in StorageTransactionRepository.__storage_transactions:
            StorageTransactionRepository.__storage_transactions[key] = transaction_obj

    @staticmethod
    def load_from_json_file(json_file: str):
        storage_transactions = StorageTransactionsDataLoader.load_from_json_file(json_file)
        for st in storage_transactions:
            StorageTransactionRepository.add(st)
            StorageRepository.add(st.storage)

    @staticmethod
    def get_all():
        return StorageTransactionRepository.__storage_transactions

    @staticmethod
    def clear():
        StorageTransactionRepository.__storage_transactions = {}