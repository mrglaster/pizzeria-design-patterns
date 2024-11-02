import time
import unittest
from datetime import datetime
import matplotlib.pyplot as plt
from src.modules.factory.process_factory.process_factory import ProcessFactory
from src.modules.repository.storage_transaction_repository import StorageTransactionRepository
from src.modules.repository.storage_turnovers_repository import StorageTurnoverRepository
from src.modules.service.generator.transactions_generator import TransactionsGenerator
from src.modules.service.init_service.start_service import StartService
from src.modules.service.managers.settings_manager import SettingsManager


class TestTurnoversPayload(unittest.TestCase):

    def test_payload(self):
        start_transactions = 250
        step = 250
        finish_transactions = 10000
        current_transactions = start_transactions
        dates = [datetime(2000, 1, 1), datetime(2010, 1, 1), datetime(2020, 1, 1)]
        sm = SettingsManager()
        StartService().create()

        x_axis = []
        y_values = [[], [], []]

        process_factory = ProcessFactory()

        def process_transactions(sm, trs, date):
            start_time = time.time()
            sm.settings.blocking_date = date
            existing_turns = process_factory.execute_process("storage_turnover_til_blocking_date", trs, True)
            result = process_factory.execute_process("storage_turnover_til_higher_date", existing_turns, False,
                                                     datetime.utcnow())
            assert len(result)
            StorageTurnoverRepository.clear()
            StorageTransactionRepository.clear()
            end_time = time.time()
            elapsed_time = end_time - start_time
            return elapsed_time

        while current_transactions < finish_transactions:
            x_axis.append(current_transactions)
            transactions = TransactionsGenerator.create_storage_transactions(current_transactions, False)
            for i in range(3):
                time_spent = process_transactions(sm, transactions, dates[i])
                y_values[i].append(time_spent)
            current_transactions += step

        assert len(x_axis)
        assert len(y_values[0]) == len(y_values[1]) == len(y_values[2])
        plt.plot(x_axis, y_values[0])
        plt.plot(x_axis, y_values[1])
        plt.plot(x_axis, y_values[2])
        plt.show()