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
        transactions_all = TransactionsGenerator.create_storage_transactions(current_transactions, False)
        x_axis = []
        y_values = [[], [], []]

        process_factory = ProcessFactory()

        def process_transactions(sm, trs, date):
            sm.settings.blocking_date = date
            existing_turns = process_factory.execute_process("storage_turnover_til_blocking_date", trs, True)
            start_time = time.time()
            result = process_factory.execute_process("storage_turnover_til_higher_date", existing_turns, False,
                                                     datetime.utcnow())
            end_time = time.time()
            assert len(result)
            StorageTurnoverRepository.clear()
            StorageTransactionRepository.clear()
            elapsed_time = end_time - start_time
            return elapsed_time

        while current_transactions < finish_transactions:
            x_axis.append(current_transactions)
            current_transactions_list = transactions_all[:current_transactions]
            for i in range(3):
                time_spent = process_transactions(sm, current_transactions_list, dates[i])
                y_values[i].append(time_spent)
            current_transactions += step

        assert len(x_axis)
        assert len(y_values[0]) == len(y_values[1]) == len(y_values[2])

        plt.plot(x_axis, y_values[0], label="Дата 2000-01-01")
        plt.plot(x_axis, y_values[1], label="Дата 2010-01-01")
        plt.plot(x_axis, y_values[2], label="Дата 2020-01-01")

        plt.title("Измерение производительности")
        plt.xlabel("Количество транзакций")
        plt.ylabel("Время выполнения (секунды)")
        plt.legend()

        plt.show()

