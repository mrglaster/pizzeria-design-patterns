import unittest
from datetime import datetime
from src.modules.factory.process_factory.process_factory import ProcessFactory
from src.modules.repository.storage_address_repository import StorageAddressRepository
from src.modules.repository.storage_repository import StorageRepository
from src.modules.repository.storage_transaction_repository import StorageTransactionRepository
from src.modules.service.init_service.start_service import StartService


class TestStorageTurnovers(unittest.TestCase):
    def test_transactions_initialization(self):
        start_service = StartService()
        start_service.create()
        assert StorageTransactionRepository.get_all().values() is not None
        assert StorageRepository.get_all().values()
        assert StorageAddressRepository.get_all().values() is not None

    def test_created_turnovers(self):
        start_service = StartService()
        start_service.create()
        storage_transactions = list(StorageTransactionRepository.get_all().values())
        assert len(storage_transactions) == 4
        process_factory = ProcessFactory()
        turns = process_factory.execute_process("storage_turnover", storage_transactions)
        assert len(turns) == 2
        assert turns[0].turnover == -37.96000000000001
        assert turns[1].turnover == 25.79

    def test_get_until_blocking_date(self):
        start_service = StartService()
        start_service.create()
        storage_transactions = list(StorageTransactionRepository.get_all().values())
        process_factory = ProcessFactory()
        turns = process_factory.execute_process("storage_turnover_til_blocking_date", storage_transactions)
        assert len(turns) == 2
        assert turns[0].turnover == -51.620000000000005
        assert turns[1].turnover == 25.79

    def test_calculate_turnovers_with_reuse(self):
        start_service = StartService()
        start_service.create()
        storage_transactions = list(StorageTransactionRepository.get_all().values())
        process_factory = ProcessFactory()
        existing_turns = process_factory.execute_process("storage_turnover_til_blocking_date", storage_transactions,
                                                         True)
        result = process_factory.execute_process("storage_turnover_til_higher_date", existing_turns, False,
                                                 datetime.utcnow())
        assert len(result) == 2
        assert result[0].turnover == -37.96000000000001
        assert result[1].turnover == 25.79
