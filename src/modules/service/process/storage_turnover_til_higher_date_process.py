import datetime
from collections import defaultdict
from src.modules.domain.enum.filter_types import FilterType
from src.modules.domain.turnover.storage_turnover import StorageTurnover
from src.modules.prototype.domain_prototype import DomainPrototype
from src.modules.repository.storage_transaction_repository import StorageTransactionRepository
from src.modules.repository.storage_turnovers_repository import StorageTurnoverRepository
from src.modules.service.managers.settings_manager import SettingsManager
from src.modules.service.process.abstract import AbstractProcess
from src.modules.service.process.storage_turnover_all_process import StorageTurnoverProcess


class StorageTurnoverTilHigherDateProcess(AbstractProcess):
    @staticmethod
    def calculate(existing_turnovers, add_to_repository=False, *kwargs):
        date = kwargs[0]
        all_transactions = list(StorageTransactionRepository.get_all().values())
        proto = DomainPrototype()
        proto.create(all_transactions)
        data = proto.filter_by(field_name='transaction_time', value=SettingsManager().settings.blocking_date,
                               filter_type=FilterType.GREATER_THAN).filter_by('transaction_time', value=date,
                                                                              filter_type=FilterType.LESS_THAN).get_data()
        turns = StorageTurnoverProcess.calculate(data)
        return StorageTurnoverTilHigherDateProcess.consolidate_turnovers(existing_turnovers, turns)

    @staticmethod
    def consolidate_turnovers(existing_transactions, new_transactions):
        consolidated_turnovers = defaultdict(float)

        for transaction in existing_transactions:
            key = (transaction.storage, transaction.nomenclature, transaction.measurement_unit)
            consolidated_turnovers[key] += transaction.turnover

        for transaction in new_transactions:
            key = (transaction.storage, transaction.nomenclature, transaction.measurement_unit)
            consolidated_turnovers[key] += transaction.turnover

        result = [
            StorageTurnover.create(
                storage=key[0],
                turnover=turnover,
                nomenclature=key[1],
                measurement_unit=key[2]
            )
            for key, turnover in consolidated_turnovers.items()
        ]
        return result
