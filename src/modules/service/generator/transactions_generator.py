import random
from datetime import datetime, timedelta
from typing import List
from src.modules.domain.enum.storage_types import TransactionType
from src.modules.domain.transaction.storage_transaction import StorageTransaction
from src.modules.repository.nomenclature_repository import NomenclatureRepository
from src.modules.repository.storage_repository import StorageRepository
from src.modules.repository.storage_transaction_repository import StorageTransactionRepository


class TransactionsGenerator:

    @staticmethod
    def generate_random_date(start: datetime, end: datetime) -> datetime:
        """Generate a random datetime between two datetime objects."""
        delta = end - start
        random_seconds = random.randint(0, int(delta.total_seconds()))
        return start + timedelta(seconds=random_seconds)

    @staticmethod
    def generate_sorted_dates(count: int) -> List[str]:
        """Generate a sorted list of random dates as strings in the desired format."""
        start_date = datetime(1990, 1, 1)
        end_date = datetime.now()
        dates = [TransactionsGenerator.generate_random_date(start_date, end_date) for _ in range(count)]
        sorted_dates = sorted(dates)
        return [date.strftime('%Y-%m-%d %H:%M:%S.%f') for date in sorted_dates]

    @staticmethod
    def create_storage_transactions(count: int, add_to_repository: bool = False) -> List[StorageTransaction]:
        """Generate a list of StorageTransaction instances with random data and sorted dates."""
        transaction_dates = TransactionsGenerator.generate_sorted_dates(count)
        transactions = []

        nomenclatures = list(NomenclatureRepository.get_all().values())
        storages = list(StorageRepository.get_all().values())
        transaction_types = [TransactionType.INCOMING, TransactionType.OUTGOING]

        for date in transaction_dates:
            storage = random.choice(storages)
            nomenclature = random.choice(nomenclatures)
            measurement_unit = nomenclature.measurement_unit
            amount = round(random.uniform(1.0, 100.0), 2)
            transaction_type = random.choice(transaction_types)
            transaction_name = "Прирост" if transaction_type == TransactionType.INCOMING else "Уход"
            transaction_name += f" {nomenclature.name}"
            transaction = StorageTransaction.create(
                storage=storage,
                nomenclature=nomenclature,
                amount=amount,
                transaction_type=transaction_type,
                measurement_unit=measurement_unit,
                time=date,
                name=transaction_name
            )
            if add_to_repository:
                StorageTransactionRepository.add(transaction)
            transactions.append(transaction)
        return transactions
