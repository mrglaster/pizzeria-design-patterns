from collections import defaultdict
from src.modules.domain.enum.filter_types import FilterType
from src.modules.domain.turnover.storage_turnover import StorageTurnover
from src.modules.prototype.domain_prototype import DomainPrototype
from src.modules.repository.storage_transaction_repository import StorageTransactionRepository
from src.modules.service.managers.settings_manager import SettingsManager
from src.modules.service.process.turnovers.abstract import AbstractProcess
from src.modules.service.process.turnovers.storage_turnover_all_process import StorageTurnoverProcess


class StorageTurnoverTilHigherDateProcess(AbstractProcess):
    @staticmethod
    def calculate(existing_turnovers, add_to_repository=False, *kwargs):
        date = kwargs[0]
        filter_action = None
        storage_name = None
        if len(kwargs) == 3:
            start_date = kwargs[1]
            filter_action = "storage|name"
            storage_name = kwargs[2]
        else:
            start_date = SettingsManager().settings.blocking_date

        all_transactions = list(StorageTransactionRepository.get_all().values())
        proto = DomainPrototype()
        proto.create(all_transactions)
        data = proto.filter_by(field_name='transaction_time', value=start_date,
                               filter_type=FilterType.GREATER_THAN).filter_by('transaction_time', value=date,
                                                                              filter_type=FilterType.LESS_THAN)
        if filter_action:
            data = data.filter_by(field_name=filter_action, filter_type=FilterType.EQUALS, value=storage_name)
        data = data.get_data()
        turns = StorageTurnoverProcess.calculate(data)
        return StorageTurnoverTilHigherDateProcess.consolidate_turnovers(existing_turnovers, turns)

    @staticmethod
    def consolidate_turnovers(existing_turnovers, new_turnovers):
        consolidated_turnovers = defaultdict(float)

        for turnover in existing_turnovers:
            key = (turnover.storage, turnover.nomenclature, turnover.measurement_unit)
            consolidated_turnovers[key] += turnover.turnover

        for turnover in new_turnovers:
            key = (turnover.storage, turnover.nomenclature, turnover.measurement_unit)
            consolidated_turnovers[key] += turnover.turnover

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
