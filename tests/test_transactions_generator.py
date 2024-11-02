import unittest

from src.modules.service.generator.transactions_generator import TransactionsGenerator
from src.modules.service.init_service.start_service import StartService


class TransactionsGeneratorTest(unittest.TestCase):
    def test_check_transactions_generation(self):
        count = 10000
        StartService().create()
        transactions = TransactionsGenerator.create_storage_transactions(count)
        assert len(transactions) == count
        for i in range(1, count):
            assert transactions[i].transaction_time >= transactions[i-1].transaction_time
            assert 'Прирост' in transactions[i].name or 'Уход' in transactions[i].name