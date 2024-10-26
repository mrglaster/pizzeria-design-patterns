import unittest
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
        assert len(storage_transactions) == 3
        process_factory = ProcessFactory()
        turns = process_factory.execute_process("storage_turnover", storage_transactions)
        assert len(turns) == 2
        assert turns[0].turnover == -51.620000000000005
        assert turns[1].turnover == 25.79
